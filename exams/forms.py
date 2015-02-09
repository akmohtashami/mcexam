from django import forms
from exams.models import Question, MadeChoice, ExamSite
from exams.widget import ExamChoiceInput, LockedExamChoiceInput
from users.models import Member
from django.utils.translation import ugettext as _
from django.core.paginator import Paginator
from django.forms import formset_factory
from codemirror.widgets import CodeMirrorTextarea


class AnswerSheetForm(forms.Form):
    question = forms.ModelChoiceField(queryset=Question.objects.filter(is_info=False),
                                      required=True,
                                      widget=forms.HiddenInput(attrs={"class": "hidden-input"}))

    def __init__(self, *args, **kwargs):
        super(AnswerSheetForm, self).__init__(*args, **kwargs)
        self.fields['answer'] = forms.ModelChoiceField(queryset=self.initial.get("question").choice_set.all(),
                                                       required=False,
                                                       widget=ExamChoiceInput)

    def clean_question(self):
        return self.initial.get("question")


class LockedAnswerSheetForm(AnswerSheetForm):

    def __init__(self, *args, **kwargs):
        super(LockedAnswerSheetForm, self).__init__(*args, **kwargs)
        self.fields['answer'] = forms.ModelChoiceField(queryset=self.initial.get("question").choice_set.all(),
                                                       required=False,
                                                       widget=LockedExamChoiceInput)


def get_answer_formset(exam, user=None, data=None, prefix=None, locked=False):
    if locked:
        answer_formset = formset_factory(
            LockedAnswerSheetForm,
            min_num=exam.question_set.filter(is_info=False).count(),
            validate_min=True,
            max_num=exam.question_set.filter(is_info=False).count(),
            validate_max=True,
        )
    else:
        answer_formset = formset_factory(
            AnswerSheetForm,
            min_num=exam.question_set.filter(is_info=False).count(),
            validate_min=True,
            max_num=exam.question_set.filter(is_info=False).count(),
            validate_max=True,
        )
    initials = []
    for question in exam.question_set.filter(is_info=False):
        if user is None:
            user_answer = None
        else:
            try:
                user_answer = user.madechoice_set.get(choice__question=question).choice
            except MadeChoice.DoesNotExist:
                user_answer = None
        initials.append({"question": question, "answer": user_answer})
    if data is None:
        formset = answer_formset(initial=initials, prefix=prefix)
    else:
        formset = answer_formset(data, initial=initials, prefix=prefix)
    return formset


def get_answer_sheet(exam, formset):
    columns = Paginator(formset, exam.questions_per_column)
    column_list = [columns.page(i) for i in columns.page_range]
    return column_list


def save_answer_sheet(formset, user):
    if not formset.is_valid():
        return False
    for form in formset:
        try:
            user_madechoice = user.madechoice_set.get(
                choice__question=form.cleaned_data["question"],
            )
            user_madechoice.delete()
        except MadeChoice.DoesNotExist:
            pass
        if form.cleaned_data["answer"] is not None:
            MadeChoice.objects.create(
                user=user,
                choice=form.cleaned_data["answer"]
            )
    return True


class OnsiteContestantForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        current_user = kwargs.pop("current_user")
        super(OnsiteContestantForm, self).__init__(*args, **kwargs)
        if current_user.is_superuser:
            self.fields['exam_site'] = forms.ModelChoiceField(
                queryset=ExamSite.objects.all(),
                label=_("Exam Site"),
                empty_label=None
            )
        else:
            self.fields['exam_site'] = forms.ModelChoiceField(
                queryset=current_user.examsite_set.all(),
                label=_("Exam Site"),
                empty_label=None
            )
        self.fields['grade'].required = True

    class Meta:
        model = Member
        fields = (
            'first_name',
            'last_name',
            'first_name_en',
            'last_name_en',
            'exam_site',
            'grade',
        )

    def save(self, commit=True):
        user = super(OnsiteContestantForm, self).save(commit=False)
        if user.id is None:
            dummy_id = Member.objects.filter(exam_site__isnull=False).count() + 1
            user.username = "dummy_imported_user_" + str(dummy_id)
            user.email = user.username + "@dummies.local"
            user.set_unusable_password()
            user.verify()
        user.school = user.exam_site.name
        if commit:
            user.save()
        return user

class CodeMirrorForm(forms.ModelForm):
    codemirror_widget = CodeMirrorTextarea(mode="stex")
    exam_pdf_template = forms.CharField(widget=codemirror_widget, label=_("PDF template"), help_text=_("Django-Tex template for creating pdf files"))
