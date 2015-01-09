from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext as _
from django.core.exceptions import ValidationError
from users.models import Member

# Create your models here.


class Exam(models.Model):
    name = models.CharField(max_length=500, verbose_name=_("Exam's name"))
    start_date = models.DateTimeField(_("Start Date"))
    end_date = models.DateTimeField(_("End Date"))

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


class Question(models.Model):
    exam = models.ForeignKey(Exam, verbose_name=_("Related exam"))
    order = models.IntegerField(unique=True,
                                verbose_name=_("Question's index"),
                                help_text=_("Questions will be shown based on their index. Also this index is shown as the question's number in exam page"))
    statement = models.CharField(max_length=10000, verbose_name=_("Question's Statement"))

    def __unicode__(self):
        return self.exam.name + " - " + _("Question #") + str(self.order)

    class Meta:
        verbose_name = _("Question")
        verbose_name_plural = _("Questions")
        ordering = ['order']


class Choice(models.Model):
    question = models.ForeignKey(Question, verbose_name="Related question")
    choice = models.CharField(max_length=10000, verbose_name=_("Choice"))
    order = models.IntegerField(verbose_name=_("Choice's index"),
                                help_text=_("Choices will be shown based on their index. Also this index is shown as choice number in exam page"))
    is_correct = models.BooleanField(default=False,
                                     verbose_name="Correct",
                                     help_text="Is this a correct answer to question?")

    def __unicode__(self):
        return self.question.__unicode__() + ": " + self.choice

    class Meta:
        verbose_name = _("Choice")
        verbose_name_plural = _("Choices")
        ordering = ['order']
        unique_together = (
            ("question", "order"),
        )


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


