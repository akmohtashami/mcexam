from django.forms import ModelChoiceField


class ShortLabelModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        if hasattr(obj, "label_for_choice_field"):
            return obj.label_for_choice_field()
        else:
            return super(ShortLabelModelChoiceField, self).label_from_instance(obj  )