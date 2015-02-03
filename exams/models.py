from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext as _
from users.models import Member
from adminsortable.models import Sortable
from adminsortable.fields import SortableForeignKey
from django.template import Template, Context
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.core.exceptions import ValidationError
import os

# Create your models here.


def get_statement_path(instance, filename):
    return os.path.join(instance.resources_dir, 'statements', filename)


class Exam(models.Model):
    name = models.CharField(max_length=500, verbose_name=_("Name"))
    activation_date = models.DateTimeField(
        _("Activation date"),
        help_text=_("After this time the exam is considered open. "
                    "Importers can download the questions and import answer sheets. "
                    "Everybody can see their answer sheet."),
    )
    online_start_date = models.DateTimeField(_("Online exam start date"))
    online_end_date = models.DateTimeField(_("Online exam end date"))
    sealing_date = models.DateTimeField(
        _("Sealing date"),
        help_text=_("After this time the exam is sealed. "
                    "Importers will no longer be able to import answer sheets"),
    )
    publish_results_date = models.DateTimeField(
        _("Result publishing date"),
        help_text=_("After this time the results and correct answers will be published "),
    )
    questions_per_column = models.PositiveIntegerField(_("Number of questions per column in answer sheet"), default=20)
    exam_pdf_template = models.TextField(
        verbose_name=_("PDF template"),
        help_text=_("Django-Tex template for creating pdf files"),
        default=""
    )
    statements_file = models.FileField(
        max_length=5000,
        upload_to=get_statement_path,
        blank=True,
        null=True,
        storage=FileSystemStorage(location='/')
    )

    class Meta:
        verbose_name = _("Exam")
        verbose_name_plural = _("Exams")
        permissions = (
            ("can_view", _("Can view exam")),
            ("can_import", _("Can import answer sheets"))
        )

    def __unicode__(self):
        return self.name

    def mode(self):
        if timezone.now() < self.activation_date:
            return -2   # exam is not activated
        elif timezone.now() < self.online_start_date:
            return -1   # online exam not started
        elif timezone.now() < self.online_end_date:
            return 0    # online exam is running
        elif timezone.now() < self.sealing_date:
            return 1    # online exam finished. exam not sealed
        elif timezone.now() < self.publish_results_date:
            return 2    # exam is sealed. results are not published
        else:
            return 3    # exam is finished and results are published

    def get_all_implicit_permissions(self, user):
        implicit_permissions = {
            "view_answer_sheet": self.mode() > -2,
            "save_answer_sheet": self.mode() == 0,
            "view_statements": self.mode() > -1,
            "import": (user.has_perm("exams:can_import", self) or user.has_perm("exams:can_import")) and
                      self.mode() > -2 and
                      self.mode < 3,
            "view_result": self.mode() >= 3
        }
        perms = []
        for perm in implicit_permissions:
            if user.has_perm("exams:change_exam", self) or \
                    user.has_perm("exams:change_exam") or \
                    implicit_permissions[perm]:
                perms.append(perm)
        return perms

    def check_implicit_permission(self, user, perm):
        return perm in self.get_all_implicit_permissions(user)

    def get_tex_file(self):
        context = {
            "exam": self
        }
        exam_template = Template(self.exam_pdf_template)
        return exam_template.render(Context(context)).encode("utf-8")

    @property
    def resources_dir(self):
        return os.path.join(settings.PRIVATE_MEDIA_ROOT, 'examfiles', str(self.id))

    def clean(self):
        if self.activation_date > self.online_start_date:
            raise ValidationError("Exam must be activated before or at the same time the online exam starts")
        if self.online_start_date > self.online_end_date:
            raise ValidationError("Online exam must start before or at the same time the online exam ends")
        if self.online_end_date > self.sealing_date:
            raise ValidationError("Online exam must end before or at the same time the exam is sealed")
        if self.sealing_date > self.publish_results_date:
            raise ValidationError("Exam must be sealed before the results are published")


class Question(Sortable):
    exam = models.ForeignKey(Exam, verbose_name=_("Related exam"))
    statement = models.TextField(verbose_name=_("Question's Statement"))
    is_info = models.BooleanField(default=False,
                                  verbose_name=_("Info"),
                                  help_text=_("If you want to put some info between some of the question write info "
                                  "in question statement and check this box"))

    def __unicode__(self):
        name = self.exam.name + " - " + _("Question #") + " " + str(self.order)
        if self.is_info:
            name += "(" + _("Info") + ")"
        return name

    @property
    def resources_dir(self):
        return os.path.join(self.exam.resources_dir, str(self.id))

    class Meta(Sortable.Meta):
        verbose_name = _("Question")
        verbose_name_plural = _("Questions")


class Choice(Sortable):
    question = SortableForeignKey(Question, verbose_name="Related question")
    choice = models.CharField(max_length=10000, verbose_name=_("Choice"))
    is_correct = models.BooleanField(default=False,
                                     verbose_name="Correct",
                                     help_text="Is this a correct answer to question?")

    def __unicode__(self):
        return self.question.__unicode__() + ": " + self.choice

    class Meta(Sortable.Meta):
        verbose_name = _("Choice")
        verbose_name_plural = _("Choices")


class MadeChoice(models.Model):
    user = models.ForeignKey(Member)
    choice = models.ForeignKey(Choice)

    def __unicode__(self):
        return self.user.__unicode__() + " - " + self.choice.question.__unicode__()

    def clean(self):
        current = MadeChoice.objects.filter(user=self.user, choice__question=self.choice.question)
        if (not current.exists()) or (self.id is not None and current[0].id == self.id):
            super(MadeChoice, self).clean()
        else:
            raise ValidationError(_("User has another answer for this question in database"),
                                  code='multiple_answer')


class ExamSite(models.Model):
    exam = models.ForeignKey(Exam, verbose_name=_("Exam"))
    importer = models.ForeignKey(Member, verbose_name=_("Importer"))
    name = models.CharField(max_length=255, verbose_name=_("Exam Site"))

    def __unicode__(self):
        return self.exam.__unicode__() + " - " + self.name

    class Meta:
        verbose_name = _("Exam Site")
        verbose_name_plural = _("Exam Sites")
