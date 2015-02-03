from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import permission_required
from guardian.decorators import permission_required as guardian_permission_required
from django.contrib import messages
from exams.models import Exam
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _


@permission_required("exams.can_view", raise_exception=True)
def list(request):
    exams_list = Exam.objects.order_by("id")
    context = {"exams_list": exams_list}
    return render(request, "exams/main_templates/list.html", context)




@guardian_permission_required("exams.can_view", (Exam, 'id', 'exam_id'), accept_global_perms=True, return_403=True)
def detail(request, exam_id):

    exam = get_object_or_404(Exam, id=exam_id)
    if exam.check_implicit_permission(request.user, "view_answer_sheet"):
        return HttpResponseRedirect(reverse("exams:answer_sheet", kwargs={"exam_id": exam_id}))
    else:
        return render(request, "exams/base_templates/blank_page.html", {"exam": exam})