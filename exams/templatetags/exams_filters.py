from django import template
from users.models import Member
from exams.models import Choice
from django.utils.translation import ugettext as _


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

