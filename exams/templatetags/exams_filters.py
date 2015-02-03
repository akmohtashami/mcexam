from django import template
from users.models import Member
from exams.models import Exam, Choice
from django.utils.translation import ugettext as _
from django.template.loader import render_to_string


register = template.Library()


@register.filter
def has_chosen(user, choice):
    if isinstance(user, Member) and isinstance(choice, Choice):
        return user.madechoice_set.filter(choice=choice).exists()

@register.filter
def choice_character(value):
    choices = [_("A"), _("B"), _("C"), _("D"), _("E")]
    if value <= 0 or value > len(choices):
        raise ValueError(_("Bad choice number"))
    return choices[value - 1]


@register.simple_tag(takes_context=True)
def exam_countdown(context):
    exam = context["exam"]
    countdown_context = {}
    if exam.mode() < 0:
        countdown_context["dest_text"] = _("Until exam starts")
        countdown_context["until"] = exam.online_start_date.isoformat()
    elif exam.mode() == 0:
        countdown_context["dest_text"] = _("Until exam ends")
        countdown_context["until"] = exam.online_end_date.isoformat()
    else:
        countdown_context["dest_text"] = _("Exam finished")
        countdown_context["until"] = None
    return render_to_string("exams/base_templates/countdown.html", countdown_context)
