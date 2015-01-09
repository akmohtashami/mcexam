from django import template
import datetime
import convertdate
from django.utils.translation import ugettext as _

register = template.Library()

@register.filter
def jalali_date(value, format_string):

    if isinstance(value, datetime.datetime):
        (jalali_year, jalali_month, jalali_day) = convertdate.persian.from_gregorian(value.year, value.month, value.day)
        format_string = format_string.replace("Y", str(jalali_year))
        format_string = format_string.replace("m", str(jalali_month).zfill(2))
        format_string = format_string.replace("d", str(jalali_day).zfill(2))
        format_string = format_string.replace("H", str(value.hour).zfill(2))
        format_string = format_string.replace("i", str(value.minute).zfill(2))
        format_string = format_string.replace("s", str(value.second).zfill(2))
        return format_string
    else:
        return format_string

@register.filter
def choice_character(value):
    choices = [_("A"), _("B"), _("C"), _("D"), _("E")]
    if value <= 0 or value > len(choices):
        raise ValueError(_("Bad choice number"))
    return choices[value - 1]