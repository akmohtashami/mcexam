from django.shortcuts import get_object_or_404, render
from guardian.decorators import permission_required as guardian_permission_required
from django.contrib import messages
from exams.models import Exam, ExamSite, ParticipantResult
from users.models import Member
from exams.forms import OnsiteContestantForm, save_answer_sheet, get_answer_sheet, get_answer_formset
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from exams.views import shared_views



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
        user_form = OnsiteContestantForm(request.POST, instance=user, current_user=request.user, current_exam=exam, prefix="user-data")
        answer_form = get_answer_formset(exam, user=user, data=request.POST, prefix="answer-data")
        if user_form.is_valid() and answer_form.is_valid():
            user = user_form.save()
            save_answer_sheet(answer_form, user)
            messages.success(request, _("Answer sheet updated successfully"))
            return HttpResponseRedirect(reverse("exams:import_panel", kwargs={"exam_id": exam_id}))
    else:
        user_form = OnsiteContestantForm(instance=user, current_user=request.user, current_exam=exam, prefix="user-data")
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
        user_form = OnsiteContestantForm(request.POST, current_user=request.user, current_exam=exam, prefix="user-data")
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
        user_form = OnsiteContestantForm(current_user=request.user, current_exam=exam, prefix="user-data")
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
    if request.user.has_perm("exams.import_all", exam):
        available_exam_sites = ExamSite.objects.filter(exam=exam)
    else:
        available_exam_sites = request.user.examsite_set.filter(exam=exam)
    context = {
        "exam": exam,
        "sites": available_exam_sites,
    }
    return render(request, "exams/importer_templates/import_panel.html", context)


@guardian_permission_required("exams.can_import", (Exam, 'id', 'exam_id'), accept_global_perms=True, return_403=True)
def results_panel(request, exam_id):
    exam = get_object_or_404(Exam, id=exam_id)
    if not exam.check_implicit_permission(request.user, "view_results"):
        raise PermissionDenied
    if request.user.has_perm("exams.see_all_results", exam):
        available_exam_sites = ExamSite.objects.filter(exam=exam)
    else:
        available_exam_sites = request.user.examsite_set.filter(exam=exam)
    context = {
        "exam": exam,
        "sites": available_exam_sites,
    }
    return render(request, "exams/importer_templates/results_panel.html", context)


@guardian_permission_required("exams.can_import", (Exam, 'id', 'exam_id'), accept_global_perms=True, return_403=True)
def user_result(request, exam_id, user_id):
    exam = get_object_or_404(Exam, id=exam_id)
    if not exam.check_implicit_permission(request.user, "view_results"):
        raise PermissionDenied
    user = get_object_or_404(Member, id=user_id)
    if request.user.has_perm("exams.see_all_results", exam) or user.is_owner(request.user):
        result = shared_views.get_user_result(exam, user)
        if result is None:
            raise Http404
        else:
            return HttpResponse(result, content_type="application/pdf")
    else:
        raise PermissionDenied


@guardian_permission_required("exams.can_import", (Exam, 'id', 'exam_id'), accept_global_perms=True, return_403=True)
def site_result(request, exam_id, site_id):
    exam = get_object_or_404(Exam, id=exam_id)
    if not exam.check_implicit_permission(request.user, "view_results"):
        raise PermissionDenied
    site = get_object_or_404(ExamSite, exam=exam, id=site_id)
    if request.user.has_perm("exams.see_all_results", exam) or site.importer == request.user:
        response = HttpResponse(shared_views.get_site_result(exam, site), content_type="application/x-zip-compressed")
        response['Content-Disposition'] = 'attachment; filename=%s' % "results.zip"
        return response
    else:
        raise PermissionDenied


@guardian_permission_required("exams.can_import", (Exam, 'id', 'exam_id'), accept_global_perms=True, return_403=True)
def site_ranking(request, exam_id, site_id):
    exam = get_object_or_404(Exam, id=exam_id)
    if not exam.check_implicit_permission(request.user, "view_results"):
        raise PermissionDenied
    site = get_object_or_404(ExamSite, exam=exam, id=site_id)
    if request.user.has_perm("exams.see_all_results", exam) or site.importer == request.user:
        context = {
            "exam": exam,
            "participants": ParticipantResult.objects.filter(user__exam_site=site),
            "show_all": True,
        }
        return render(request, "exams/base_templates/standings.html", context)
    else:
        raise PermissionDenied