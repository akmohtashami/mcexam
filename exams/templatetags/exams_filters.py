# -*- coding: utf-8 -*-
from django import template
from users.models import Member
from exams.models import Choice, Participation
from django.utils.translation import ugettext as _
from django.utils import timezone
from django.template.loader import render_to_string
import datetime

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
       	try:
               user = context["user"]
               p = Participation.objects.get(user=user,exam=exam)
               d = int(exam.duration)
               if d <= 0:
			countdown_context["dest_text"] = _("Until exam ends")
			countdown_context["until"] = exam.online_end_date.isoformat()
               else:
			delta = datetime.timedelta(minutes=d)
			end_date = p.start_date + delta
			if exam.online_end_date < end_date:
			         end_date = exam.online_end_date
			if timezone.now() <= end_date:
			         #x = (end_date-timezone.now()).isoformat()
			         #print(type(end_date-timezone.now()))
			         countdown_context["until"] = end_date.isoformat()
			         countdown_context["dest_text"] = "تا پایان آزمون شما"
			else:
			         countdown_context["dest_text"] = _("Exam finished")
			         countdown_context["until"] = None
       	except Exception:
               countdown_context["dest_text"] = _("Until exam ends")
               countdown_context["until"] = exam.online_end_date.isoformat()
    else:
        countdown_context["dest_text"] = _("Exam finished")
        countdown_context["until"] = None
    return render_to_string("exams/base_templates/countdown.html", countdown_context)

@register.assignment_tag
def is_official(exam, user):
    if user.has_perm("out_of_competition", exam):
        return False
    else:
        return True

@register.tag
def get_next_number(parser, token):
    try:
        tag_name, start_value = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError("%r tag requires a single argument" % token.contents.split()[0])
    return GetNextNumberNode(start_value)


class GetNextNumberNode(template.Node):
    def __init__(self, start_value):
        self.start_value = start_value

    def render(self, context):
        if self not in context.render_context:
            context.render_context[self] = str(self.start_value)
        val = int(context.render_context[self])
        context.render_context[self] = str(val + 1)
        return str(val)


