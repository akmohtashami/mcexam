from django.contrib import admin
from exams.models import Exam
from exams.models import Question, Choice, MadeChoice
from django import forms
from django.db import models

# Register your models here.

ChoiceFormSet = forms.inlineformset_factory(
    Question,
    Choice,
    min_num=0,
    max_num=5,
    extra=5,
)


class QuestionForm(forms.ModelForm):
    def __init__(self, **kwargs):
        super(QuestionForm, self).__init__(**kwargs)
        self.choice_formset = ChoiceFormSet(
            instance=self.instance,
            data=self.data or None,
            prefix=self.prefix + "-choices"
        )
        self.fields["statement"].widget = forms.Textarea(attrs=None)

    def has_changed(self):
        return super(QuestionForm, self).has_changed() or self.choice_formset.has_changed()

    def is_valid(self):
        return super(QuestionForm, self).is_valid() and self.choice_formset.is_valid()

    def save(self, commit=True):
        if not commit:
            raise NotImplementedError
        res = super(QuestionForm, self).save(commit=commit)
        self.choice_formset.save()
        return res


class QuestionInLine(admin.TabularInline):
    model = Question
    form = QuestionForm
    template = "exams/admin/question_form.html"
    extra = 0


class ExamAdmin(admin.ModelAdmin):
    inlines = [
        QuestionInLine,
        ]


class ChoicesInLine(admin.TabularInline):
    model = Choice

class QuestionAdmin(admin.ModelAdmin):
    inlines = [
        ChoicesInLine,
    ]
    formfield_overrides = {
        models.CharField: {'widget': forms.Textarea},
    }

admin.site.register(Exam, ExamAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(MadeChoice)