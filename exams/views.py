from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import permission_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.forms import formset_factory
from exams.models import Exam, MadeChoice
from exams.forms import AnswerForm
# Create your views here.

@permission_required("exams.can_view", raise_exception=True)
def list(request):
    exams_list = Exam.objects.order_by("id")
    context = {"exams_list": exams_list}
    return render(request, "exams/list.html", context)


def process_saving_form(questions, request):
    if request.method == "POST":
        current_user = request.user
        AnswerFormSet = formset_factory(AnswerForm,
                                        min_num=questions.count(),
                                        validate_min=True,
                                        max_num=questions.count(),
                                        validate_max=True,
                                        )
        initial = [{'question': q} for q in questions]
        formset = AnswerFormSet(request.POST,
                                initial=initial,
                                )

        if formset.is_valid():
            for form in formset:
                try:
                    current_user_madechoice = current_user.madechoice_set.get(
                        choice__question=form.cleaned_data["question"],
                    )
                    current_user_madechoice.delete()
                except MadeChoice.DoesNotExist:
                    pass
                if form.cleaned_data["answer"] is not None:
                    MadeChoice.objects.create(
                        user=current_user,
                        choice=form.cleaned_data["answer"]
                    )


def exam_running(request, exam):
    questions = exam.question_set.all()
    current_user = request.user
    process_saving_form(questions, request)
    initials = []
    for question in questions:
        try:
            current_user_answer = current_user.madechoice_set.get(choice__question=question).choice
        except MadeChoice.DoesNotExist:
            current_user_answer = None
        initials.append({"question": question, "answer": current_user_answer})
    AnswerFormSet = formset_factory(AnswerForm,
                                    min_num=questions.count(),
                                    validate_min=True,
                                    max_num=questions.count(),
                                    validate_max=True,
                                    )
    forms = AnswerFormSet(initial=initials)
    pages = Paginator(forms, 1)
    all_pages = [pages.page(i) for i in pages.page_range]
    all_pages_orders = []
    for page in all_pages:
        pages_orders = []
        for form in page.object_list:
            pages_orders.append((form, form.initial["question"].order))
        all_pages_orders.append(pages_orders)
    context = {"exam": exam, "formset": forms, "pages": all_pages_orders}
    return render(request, "exams/running_exam.html", context)

@permission_required("exams.can_view", raise_exception=True)
def detail(request, exam_id):
    exam = get_object_or_404(Exam, pk=exam_id)
    context = {"exam": exam}
    if exam.stage() == 0:
        return exam_running(request, exam)
    else:
        return render(request, "exams/not_running_exam.html", context)
