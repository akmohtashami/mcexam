from django.shortcuts import get_object_or_404, render
from exams.models import Exam, ExamSite
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.core.urlresolvers import reverse
from django.core.exceptions import PermissionDenied
from exams.views import importer_views, contestant_views, shared_views



def list(request):
    exams_list = Exam.objects.order_by("id")
    context = {"exams_list": exams_list}
    return render(request, "exams/main_templates/list.html", context)


def detail(request, exam_id):

    exam = get_object_or_404(Exam, id=exam_id)
    if exam.check_implicit_permission(request.user, "view_answer_sheet"):
        return HttpResponseRedirect(reverse("exams:answer_sheet", kwargs={"exam_id": exam_id}))
    else:
        return render(request, "exams/base_templates/blank_page.html", {"exam": exam})


def results(request, exam_id):
    exam = get_object_or_404(Exam, id=exam_id)

    if exam.check_implicit_permission(request.user, "view_results"):
        related_sites = ExamSite.objects.filter(importer=request.user)
        if related_sites:
            return importer_views.results_panel(request, exam)
        else:
            result = shared_views.get_user_result(exam, request.user)
            if result is None:
                raise Http404
            else:
                return HttpResponse(result, content_type="application/pdf")
    else:
        raise PermissionDenied