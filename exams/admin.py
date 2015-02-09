from django.contrib import admin
from exams.models import Exam
from exams.models import Question, Choice, MadeChoice, ExamSite, ParticipantResult
from adminsortable.admin import NonSortableParentAdmin, SortableTabularInline, SortableAdmin
from guardian.admin import GuardedModelAdmin
from resources.admin import ResourceInLine
from exams.forms import CodeMirrorForm
from django.utils.translation import ugettext as _
from django.core.cache import cache
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
    actions = ("calculate_result", )
    list_display = ("__unicode__", "total_score")

    def calculate_result(self, request, queryset):
        for exam in queryset:
            exam.calculate_all_results()
            cache_name = "exam_" + str(exam.id) + "_total_score"
            cache.delete(cache_name)
            exam.calculate_total_score()
        self.message_user(request, _("Successfully computed results for selected exams"))
    calculate_result.short_description = _("Calculate results for selected exams")



class ChoicesInLine(SortableTabularInline):
    model = Choice


class QuestionAdmin(SortableAdmin):
    inlines = [
        ResourceInLine, ChoicesInLine,
    ]

    list_display = ("__unicode__", "is_info")


class ExamSiteAdmin(admin.ModelAdmin):
    list_display = ("name", "exam", "importer", "participants_count")
    list_display_links = ("name", )

class ParticipantResultAdmin(admin.ModelAdmin):
    pass

class ChoiceAdmin(SortableAdmin):
    pass

admin.site.register(Exam, ExamAdmin)
admin.site.register(ExamSite, ExamSiteAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(MadeChoice)
admin.site.register(ParticipantResult, ParticipantResultAdmin)