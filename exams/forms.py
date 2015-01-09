from django import forms
from exams.models import Question
from exams.widget import ExamChoiceInput


class AnswerForm(forms.Form):
    question = forms.ModelChoiceField(queryset=Question.objects.all(),
                                      required=True,
                                      widget=forms.HiddenInput(attrs={"class": "hidden-input"}))

    def __init__(self, *args, **kwargs):
        super(AnswerForm, self).__init__(*args, **kwargs)
        self.fields['answer'] = forms.ModelChoiceField(queryset=self.initial.get("question").choice_set.all(),
                                                       required=False,
                                                       widget=ExamChoiceInput)



    def clean_question(self):
        return self.initial.get("question")


