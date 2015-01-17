from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext as _
from django.core.exceptions import ValidationError
from users.models import Member
from adminsortable.models import Sortable
from adminsortable.fields import SortableForeignKey

# Create your models here.


class Exam(models.Model):
    name = models.CharField(max_length=500, verbose_name=_("Exam's name"))
    start_date = models.DateTimeField(_("Start Date"))
    end_date = models.DateTimeField(_("End Date"))
    question_per_column = models.PositiveIntegerField(_("Number of questions per column in answer sheet"), default=20)

    class Meta:
        verbose_name = _("Exam")
        verbose_name_plural = _("Exams")
        permissions = (
            ("can_view", _("Can user view exams")),
        )
    def __unicode__(self):
        return self.name
    def stage(self):
        #raise ValueError("%d", self.end_date, datetime.now())
        if timezone.now() < self.start_date:
            return -1  # exam hasn't started yet
        elif timezone.now() >= self.end_date:
            return 1  # exam has ended
        else:
            return 0  # exam is running


class Question(Sortable):
    exam = SortableForeignKey(Exam, verbose_name=_("Related exam"))
    statement = models.TextField(verbose_name=_("Question's Statement"))

    def __unicode__(self):
        return self.exam.name + " - " + _("Question #") + " " + str(self.order)

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


