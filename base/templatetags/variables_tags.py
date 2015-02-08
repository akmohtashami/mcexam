from django import template
from django.utils.translation import ugettext as _
from django.template.loader import render_to_string

register = template.Library()

@register.tag
def set_var(parser, token):
    try:
        tag_name, var_name, value = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError("%r tag requires three argument" % token.contents.split()[0])
    return GetVariableNode(tag_name, var_name, value)

@register.tag
def get_var(parser, token):
    try:
        tag_name, var_name = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError("%r tag requires two argument" % token.contents.split()[0])
    return GetVariableNode(tag_name, var_name)

@register.tag
def add_var(parser, token):
    try:
        tag_name, var_name, value = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError("%r tag requires three argument" % token.contents.split()[0])
    return GetVariableNode(tag_name, var_name, value)

@register.tag
def make_var(parser, token):
    try:
        tag_name, var_name, value = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError("%r tag requires three argument" % token.contents.split()[0])
    return GetVariableNode(tag_name, var_name, value)


class GetVariableNode(template.Node):
    def __init__(self, operation, var_name, param=None):
        self.operation = operation
        self.var_name = var_name
        self.param = param

    def render(self, context):
        context_name = "var_" + self.var_name
        if context_name not in context.render_context:
            if self.operation != "set_var" and self.operation != "make_var":
                raise template.TemplateSyntaxError("Variable %r is not defined" % self.param)
        if self.operation == "set_var":
            context.render_context[context_name] = self.param
        elif self.operation == "make_var":
            new_var_context = "var_" + self.param
            if new_var_context not in context.render_context:
                raise template.TemplateSyntaxError("Variable %r is not defined" % self.param)
            context.render_context[context_name] = context.render_context[new_var_context]
        elif self.operation == "get_var":
            return context.render_context[context_name]
        elif self.operation == "add_var":
            cur_value = float(context.render_context[context_name])
            cur_value += float(self.param)
            context.render_context[context_name] = str(cur_value)
        return ""