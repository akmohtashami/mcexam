from django.contrib import admin
from exams.models import Exam
from exams.models import Question, Choice, MadeChoice
import django_jalali.admin as jadmin

# Register your models here.
admin.site.register(Exam)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(MadeChoice)