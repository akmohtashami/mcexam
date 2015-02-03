from django.core.urlresolvers import resolve
from django.shortcuts import get_object_or_404
from exams.models import Exam


def exam_implicit_permissions(request):
    rm = resolve(request.path)
    try:
        exam = get_object_or_404(Exam, id=rm.kwargs["exam_id"])
        return {"exam_implicit_permissions": exam.get_all_implicit_permissions(request.user)}
    except:
        return {}
