from django.shortcuts import get_object_or_404, render
from exams.models import Exam
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse



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


