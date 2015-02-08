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
from django.core.cache import cache
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
            "import": (user.has_perm("exams.can_import", self) or user.has_perm("exams.can_import")) and
                      self.mode() > -2 and
                      self.mode() < 3,
            "view_results": self.mode() >= 3
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

    def get_statements_tex_file(self):
        context = {
            "exam": self
        }
        exam_template = Template(self.exam_pdf_template)
        return exam_template.render(Context(context)).encode("utf-8")

    @property
    def resources_dir(self):
        return os.path.join(settings.PRIVATE_MEDIA_ROOT, 'examfiles', str(self.id))

    def add_tex_resources_to_environ(self, base_env=os.environ):
        env = base_env.copy()
        xelatex_path = getattr(settings, "XELATEX_BIN_PATH", None)
        if xelatex_path is not None:
            env["PATH"] = os.pathsep.join([xelatex_path, env["PATH"]])
        env["TEXINPUTS"] = self.resources_dir + "//:" + env.get("TEXINPUTS", "")
        env["TTFONTS"] = self.resources_dir + "//:" + env.get("TTFONTS", "")
        env["OPENTYPEFONTS"] = self.resources_dir + "//:" + env.get("OPENTYPEFONTS", "")
        return env

    def calculate_user_score(self, user):
        try:
            result = ParticipantResult.objects.get(exam=self, user=user)
        except ParticipantResult.DoesNotExist:
            result = ParticipantResult(user=user, exam=self)
        result.score = 0
        result.correct = 0
        result.wrong = 0
        for question in self.question_set.filter(is_info=False):
            try:
                marked_choice = MadeChoice.objects.get(user=user, choice__in=question.choice_set.all()).choice
                if marked_choice.is_correct:
                    result.correct += 1
                    result.score += question.correct_score
                else:
                    result.wrong += 1
                    result.score -= question.wrong_penalty
            except MadeChoice.DoesNotExist:
                pass
        result.rank = 0
        result.save()

    def calculate_all_results(self):
        """
        This calculates the score and rank of all users who have at least one answered question
        """

        #Calculating score
        for user in Member.objects.all():
            user_cache = "exam_" + str(self.id) + "_user_" + str(user.id) + "_result"
            cache.delete(user_cache)
            if user.exam_site is not None:
                site_cache = "exam_" + str(self.id) + "_site_" + str(user.exam_site.id) + "_result"
                cache.delete(site_cache)
            self.calculate_user_score(user)

        #Calculating rank
        participants = ParticipantResult.objects.filter(exam=self)
        last_participant = None
        current_rank = 1
        for participant in participants:
            if last_participant is None or last_participant.score > participant.score:
                participant.rank = current_rank
            else:
                participant.rank = last_participant.rank
            participant.save()
            last_participant = participant
            current_rank += 1

    def calculate_total_score(self):
        total_score = 0
        for question in self.question_set.filter(is_info=False):
            total_score += question.correct_score
        return total_score

    @property
    def total_score(self):
        cache_name = "exam_" + str(self.id) + "_total_score"
        if cache.get(cache_name) is None:
            total_score = self.calculate_total_score()
            cache.set(cache_name, total_score, None)
        return cache.get(cache_name)

    def get_user_question_details(self, user):
        question_list = []
        for question in self.question_set.filter(is_info=False):
            try:
                marked_choice = MadeChoice.objects.get(user=user, choice__in=question.choice_set.all()).choice
            except MadeChoice.DoesNotExist:
                marked_choice = None
            question_list.append((question, marked_choice))
        return question_list

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
    correct_score = models.PositiveSmallIntegerField(
        verbose_name=_("Correct Answer Score"),
        help_text=_("Amount of score which is increased for correct answer"),
        default=4,
    )
    wrong_penalty = models.PositiveSmallIntegerField(
        verbose_name=_("Wrong Answer Penalty"),
        help_text=_("Amount of score which is decreased for incorrent answer"),
        default=1
    )

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
        name = self.question.__unicode__() + ": " + self.choice
        if self.is_correct:
            name += "(" + _("Correct") + ")"
        return name

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

    class Meta:
        ordering = ['user', 'choice__question__exam', 'choice__question']


class ExamSite(models.Model):
    exam = models.ForeignKey(Exam, verbose_name=_("Exam"))
    importer = models.ForeignKey(Member, verbose_name=_("Importer"))
    name = models.CharField(max_length=255, verbose_name=_("Exam Site"))

    def __unicode__(self):
        return self.name

    def participants_count(self):
        return len(Member.objects.filter(exam_site=self))
    participants_count.short_description = _("Number of participants")

    class Meta:
        verbose_name = _("Exam Site")
        verbose_name_plural = _("Exam Sites")


class ParticipantResult(models.Model):
    exam = models.ForeignKey(Exam, verbose_name=_("Exam"))
    user = models.ForeignKey(Member, verbose_name=_("Participant"))
    score = models.PositiveIntegerField(verbose_name=_("Score"))
    correct = models.PositiveIntegerField(verbose_name=_("Correct answers"))
    wrong = models.PositiveIntegerField(verbose_name=_("Wrong answers"))
    rank = models.PositiveIntegerField(verbose_name=_("Rank"))

    def __unicode__(self):
        return self.exam.__unicode__() + ": " + self.user.get_full_name()

    class Meta:
        ordering = ['exam', '-score']
