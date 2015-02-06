from django.shortcuts import get_object_or_404, render
from guardian.decorators import permission_required as guardian_permission_required
from django.contrib import messages
from exams.models import Exam
from users.models import Member
from exams.forms import OnsiteContestantForm, save_answer_sheet, get_answer_sheet, get_answer_formset
from django.http import HttpResponseRedirect
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _

@guardian_permission_required("exams.can_import", (Exam, 'id', 'exam_id'), accept_global_perms=True, return_403=True)
def delete_data(request, exam_id, user_id):
    exam = get_object_or_404(Exam, id=exam_id)
    if not exam.check_implicit_permission(request.user, "import"):
        raise PermissionDenied
    user = get_object_or_404(Member, id=user_id)
    if not user.is_owner(request.user):
        raise PermissionDenied
    else:
        user.delete()
        messages.success(request, _("Answer sheet was removed successfully"))
    return HttpResponseRedirect(reverse("exams:import_panel", kwargs={"exam_id": exam_id}))


@guardian_permission_required("exams.can_import", (Exam, 'id', 'exam_id'), accept_global_perms=True, return_403=True)
def edit_data(request, exam_id, user_id):
    exam = get_object_or_404(Exam, id=exam_id)
    if not exam.check_implicit_permission(request.user, "import"):
        raise PermissionDenied
    user = get_object_or_404(Member, id=user_id)
    if not user.is_owner(request.user):
        raise PermissionDenied
    if request.method == "POST":
        user_form = OnsiteContestantForm(request.POST, instance=user, current_user=request.user, prefix="user-data")
        answer_form = get_answer_formset(exam, user=user, data=request.POST, prefix="answer-data")
        if user_form.is_valid() and answer_form.is_valid():
            user = user_form.save()
            save_answer_sheet(answer_form, user)
            messages.success(request, _("Answer sheet updated successfully"))
            return HttpResponseRedirect(reverse("exams:import_panel", kwargs={"exam_id": exam_id}))
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

    return render(request, "exams/importer_templates/edit_data.html", context)


@guardian_permission_required("exams.can_import", (Exam, 'id', 'exam_id'), accept_global_perms=True, return_403=True)
def add_data(request, exam_id):
    exam = get_object_or_404(Exam, id=exam_id)
    if not exam.check_implicit_permission(request.user, "import"):
        raise PermissionDenied
    if request.method == "POST":
        user_form = OnsiteContestantForm(request.POST, current_user=request.user, prefix="user-data")
        answer_form = get_answer_formset(exam, data=request.POST, prefix="answer-data")
        if user_form.is_valid() and answer_form.is_valid():
            user = user_form.save()
            save_answer_sheet(answer_form, user)
            messages.success(request, _("Answer sheet added successfully"))
            if 'addagain_button' in request.POST:
                return HttpResponseRedirect(reverse("exams:add_data", kwargs={"exam_id": exam_id}))
            else:
                return HttpResponseRedirect(reverse("exams:import_panel", kwargs={"exam_id": exam_id}))
    else:
        user_form = OnsiteContestantForm(current_user=request.user, prefix="user-data")
        answer_form = get_answer_formset(exam, prefix="answer-data")

    answer_sheet_full_columns = get_answer_sheet(exam, answer_form)

    context = {"exam": exam,
               "user_form": user_form,
               "answer_sheet_forms": answer_form,
               "answer_sheet_full_columns": answer_sheet_full_columns,
               }
    return render(request, "exams/importer_templates/add_data.html", context)

@guardian_permission_required("exams.can_import", (Exam, 'id', 'exam_id'), accept_global_perms=True, return_403=True)
def import_panel(request, exam_id):
    exam = get_object_or_404(Exam, id=exam_id)
    if not exam.check_implicit_permission(request.user, "import"):
        raise PermissionDenied
    available_exam_sites = request.user.examsite_set.all()
    site_user_list = []
    for site in available_exam_sites:
        available_onsite_users = site.member_set.filter(exam_site=site)
        site_user_list.append((site, available_onsite_users))
    context = {
        "exam": exam,
        "sites": site_user_list,
    }
    return render(request, "exams/importer_templates/import_panel.html", context)