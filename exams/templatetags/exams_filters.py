from django import template
from users.models import Member
from exams.models import Choice


register = template.Library()


@register.filter
def has_chosen(user, choice):
    if isinstance(user, Member) and isinstance(choice, Choice):
        return user.madechoice_set.filter(choice=choice).exists()