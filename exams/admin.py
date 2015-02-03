from django.contrib import admin
from exams.models import Exam
from exams.models import Question, Choice, MadeChoice, ExamSite
from adminsortable.admin import NonSortableParentAdmin, SortableTabularInline, SortableAdmin
from guardian.admin import GuardedModelAdmin
from resources.admin import ResourceInLine
from exams.forms import CodeMirrorForm
# Register your models here.



class QuestionInLine(SortableTabularInline):
    model = Question
    extra = 0


class ExamAdmin(GuardedModelAdmin, NonSortableParentAdmin):
    inlines = [
        ResourceInLine, QuestionInLine,
        ]
    change_form_template_extends = GuardedModelAdmin.change_form_template
    form = CodeMirrorForm


class ChoicesInLine(SortableTabularInline):
    model = Choice


class QuestionAdmin(SortableAdmin):
    inlines = [
        ResourceInLine, ChoicesInLine,
    ]
    list_display = ("__unicode__", "is_info")
    """
    def __init__(self, *args, **kwargs):

        self.list_display += ("is_info", )
        super(QuestionAdmin, self).__init__(*args, **kwargs)
    """

admin.site.register(Exam, ExamAdmin)
admin.site.register(ExamSite)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(MadeChoice)