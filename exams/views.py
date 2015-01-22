from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import permission_required
from guardian.decorators import permission_required as guardian_permission_required
from django.contrib import messages
from exams.models import Exam, ExamSite
from users.models import Member
from exams.forms import OnsiteContestantForm, save_answer_sheet, get_answer_sheet, get_answer_formset
from django.http import HttpResponseRedirect
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _


@permission_required("exams.can_view", raise_exception=True)
def list(request):
    exams_list = Exam.objects.order_by("id")
    context = {"exams_list": exams_list}
    return render(request, "exams/list.html", context)


def exam_running(request, exam):
    if request.method == "POST":
        forms = get_answer_formset(exam, request.user, request.POST)
        if save_answer_sheet(forms, request.user):
            messages.success(request, _("Answers saved successfully"))
        else:
            messages.error(request, _("A problem occured. Please try again"))
    else:
        forms = get_answer_formset(exam, request.user)
    full_columns = get_answer_sheet(exam, forms)
    context = {"exam": exam, "formset": forms, "columns": full_columns}
    return render(request, "exams/running_exam.html", context)

@guardian_permission_required("exams.can_import", (Exam, 'id', 'exam_id'), accept_global_perms=True, return_403=True)
def delete_data(request, exam_id, user_id):
    user = get_object_or_404(Member, id=user_id)
    if not user.is_owner(request.user):
        raise PermissionDenied
    else:
        user.delete()
        messages.success(request, "Data was removed successfully")
    return HttpResponseRedirect(reverse("exams:import", kwargs={"exam_id": exam_id}))


@guardian_permission_required("exams.can_import", (Exam, 'id', 'exam_id'), accept_global_perms=True, return_403=True)
def edit_data(request, exam_id, user_id):
    exam = get_object_or_404(Exam, id=exam_id)
    user = get_object_or_404(Member, id=user_id)
    if not user.is_owner(request.user):
        raise PermissionDenied

    if request.method == "POST":
        user_form = OnsiteContestantForm(request.POST, instance=user, current_user=request.user, prefix="user-data")
        answer_form = get_answer_formset(exam, user=user, data=request.POST, prefix="answer-data")
        if user_form.is_valid() and answer_form.is_valid():
            user = user_form.save()
            save_answer_sheet(answer_form, user)
            messages.success(request, _("Updated successfully"))
            return HttpResponseRedirect(reverse("exams:import", kwargs={"exam_id": exam_id}))
    else:
        user_form = OnsiteContestantForm(instance=user, current_user=request.user, prefix="user-data")
        answer_form = get_answer_formset(exam, user, prefix="answer-data")

    answer_sheet_full_columns = get_answer_sheet(exam, answer_form)

    context = {"exam": exam,
               "user_id": user_id,
               "user_form": user_form,
               "answer_sheet_forms": answer_form,
               "answer_sheet_full_columns": answer_sheet_full_columns,
               }

    return render(request, "exams/exam_edit_data.html", context)


@guardian_permission_required("exams.can_import", (Exam, 'id', 'exam_id'), accept_global_perms=True, return_403=True)
def add_data(request, exam_id):
    exam = get_object_or_404(Exam, id=exam_id)
    if request.method == "POST":
        user_form = OnsiteContestantForm(request.POST, current_user=request.user, prefix="user-data")
        answer_form = get_answer_formset(exam, data=request.POST, prefix="answer-data")
        if user_form.is_valid() and answer_form.is_valid():
            user = user_form.save()
            save_answer_sheet(answer_form, user)
            messages.success(request, _("Added successfully"))
            return HttpResponseRedirect(reverse("exams:import", kwargs={"exam_id": exam_id}))
            user_form = OnsiteContestantForm(current_user=request.user, prefix="user-data")
            answer_form = get_answer_formset(exam, prefix="answer-data")
    else:
        user_form = OnsiteContestantForm(current_user=request.user, prefix="user-data")
        answer_form = get_answer_formset(exam, prefix="answer-data")

    answer_sheet_full_columns = get_answer_sheet(exam, answer_form)

    context = {"exam": exam,
               "user_form": user_form,
               "answer_sheet_forms": answer_form,
               "answer_sheet_full_columns": answer_sheet_full_columns,
               }
    return render(request, "exams/exam_add_data.html", context)

@guardian_permission_required("exams.can_import", (Exam, 'id', 'exam_id'), accept_global_perms=True, return_403=True)
def import_data(request, exam_id):
    exam = get_object_or_404(Exam, id=exam_id)
    if exam.mode() >= 2:
        messages.error(request, _("You can't import data for this exam anymore"))
        return HttpResponseRedirect(reverse("exams:list"))
    available_exam_sites = request.user.examsite_set.all()
    site_user_list = []
    for site in available_exam_sites:
        available_onsite_users = site.member_set.filter(exam_site=site)
        site_user_list.append((site, available_onsite_users))
    context = {
        "exam": exam,
        "sites": site_user_list,
    }
    return render(request, "exams/exam_manage.html", context)

@guardian_permission_required("exams.can_view", (Exam, 'id', 'exam_id'), accept_global_perms=True, return_403=True)
def detail(request, exam_id):
    exam = get_object_or_404(Exam, id=exam_id)
    if not request.user.is_superuser and request.user.has_perm("exams.can_import", exam):
        return HttpResponseRedirect(reverse("exams:import", kwargs={"exam_id": exam_id}))
    elif exam.mode() <= -1:
        messages.error(request, _("This exam hasn't started yet"))
    elif exam.mode() == 0:
        return exam_running(request, exam)
    elif exam.mode() >= 1:
        messages.error(request, _("This exam has ended"))
    return HttpResponseRedirect(reverse("exams:list"))
