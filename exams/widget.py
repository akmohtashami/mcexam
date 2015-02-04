from django.forms.widgets import Widget
from django.utils.html import format_html, mark_safe
from django.utils.encoding import smart_text
from exams.templatetags.exams_filters import choice_character


class ExamChoiceInput(Widget):
    def __init__(self, attrs=None):
        super(ExamChoiceInput, self).__init__(attrs)

    def render(self, name, value, attrs=None):
        output = []
        option_index = 1
        for option_value, option_label in self.choices:
            if not option_value:
                continue
            radio_code = '<td><input autocomplete="off" class="hidden-input" type="radio" name="{0}" data-identifier="{0}-{1}-choice" value="{1}"'
            try:
                if option_value == int(value):
                    radio_code += ' checked=true'
            except:
                pass
            radio_code += '>'
            output.append(format_html(radio_code, name, str(option_value)))
            label_code = u'<div data-correspond="{0}-{1}-choice" class="choice'
            try:
                if option_value == int(value):
                    label_code += ' marked'
            except:
                pass
            label_code += '" >{2}</div></td>'
            output.append(format_html(label_code, name, str(option_value), choice_character(option_index)))
            option_index += 1
        return mark_safe('\n'.join(output))


class LockedExamChoiceInput(Widget):
    def __init__(self, attrs=None):
        super(LockedExamChoiceInput, self).__init__(attrs)

    def render(self, name, value, attrs=None):
        output = []
        option_index = 1
        for option_value, option_label in self.choices:
            if not option_value:
                continue
            label_code = u'<td><div class="choice locked'
            try:
                if option_value == int(value):
                    label_code += ' marked'
            except:
                pass
            label_code += '" >{2}</div></td>'
            output.append(format_html(label_code, name, str(option_value), choice_character(option_index)))
            option_index += 1
        return mark_safe('\n'.join(output))
