# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, render
from django.contrib import messages
from exams.models import Exam, Participation
from exams.forms import save_answer_sheet, get_answer_sheet, get_answer_formset
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from django.utils import timezone
from exams.views import shared_views
import os
import magic


def answer_sheet(request, exam_id):
    exam = get_object_or_404(Exam, id=exam_id)
    if not exam.check_implicit_permission(request.user, "view_answer_sheet"):
        raise PermissionDenied
    if not exam.check_implicit_permission(request.user, "save_answer_sheet"):
        locked = True
    else:
        locked = False
    if exam.mode() == 0:
            try:
                p = Participation.objects.get(user=request.user,exam=exam)
            except Participation.DoesNotExist:
                p = Participation(user=request.user,exam=exam, start_date = timezone.now())
                p.save()
                messages.success(request, "آزمون برای شما شروع شد!")
    if request.method == "POST":
        if locked:
            messages.error(request, _("The exam is not running right now. You cannot submit answers"))
        else:
            forms = get_answer_formset(exam, request.user, request.POST, locked=locked)
            if save_answer_sheet(forms, request.user):
                messages.success(request, _("Answers saved successfully"))
            else:
                messages.error(request, _("A problem occured. Please try again"))
        return HttpResponseRedirect(reverse("exams:answer_sheet", kwargs={"exam_id": exam_id}))
    else:
        forms = get_answer_formset(exam, request.user, locked=locked)
    full_columns = get_answer_sheet(exam, forms)
    context = {"exam": exam, "formset": forms, "columns": full_columns, "user": request.user}
    return render(request, "exams/main_templates/answer_sheet.html", context)


def statements(request, exam_id):
    exam = get_object_or_404(Exam, id=exam_id)
    if not exam.check_implicit_permission(request.user, "view_statements"):
        raise PermissionDenied
    if not exam.statements_file:
        raise Http404
    if exam.mode() == 0:
            try:
                p = Participation.objects.get(user=request.user,exam=exam)
            except Participation.DoesNotExist:
                p = Participation(user=request.user,exam=exam, start_date = timezone.now())
                p.save()
                messages.success(request, "آزمون برای شما شروع شد!")
    real_file_name, real_file_ext = os.path.splitext(exam.statements_file.name)
    statements_name = "statements_" + exam_id + real_file_ext
    response = HttpResponse(exam.statements_file, content_type=magic.from_buffer(exam.statements_file.read(), mime=True))
    response['Content-Disposition'] = 'attachment; filename=%s' % statements_name
    return response


def results(request, exam_id):
    exam = get_object_or_404(Exam, id=exam_id)
    if exam.check_implicit_permission(request.user, "view_results"):
        result = shared_views.get_user_result(exam, request.user)
        if result is None:
            raise Http404
        else:
            return HttpResponse(result, content_type="application/pdf")
    else:
        raise PermissionDenied
