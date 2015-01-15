from django.contrib import admin
from exams.models import Exam
from exams.models import Question, Choice, MadeChoice
from django import forms
from django.db import models
from adminsortable.admin import NonSortableParentAdmin, SortableTabularInline, SortableAdmin

# Register your models here.

class QuestionInLine(SortableTabularInline):
    model = Question
    extra = 0


class ExamAdmin(NonSortableParentAdmin):
    inlines = [
        QuestionInLine,
        ]


class ChoicesInLine(SortableTabularInline):
    model = Choice


class QuestionAdmin(SortableAdmin):
    inlines = [
        ChoicesInLine,
    ]

admin.site.register(Exam, ExamAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(MadeChoice)