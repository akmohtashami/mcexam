from django.contrib import admin
from django.contrib.auth.models import Group
from django.db import models
from users.models import Member
from users.forms import MemberAdminAddForm, MemberAdminChangeForm
from django.utils.translation import ugettext as _


# Register your models here.

def verify_user(modeladmin, request, queryset):
    for user in queryset:
        user.verify()
verify_user.short_description = _("Verify selected users")


class MemberAdmin(admin.ModelAdmin):
    form = MemberAdminChangeForm
    add_form = MemberAdminAddForm
    list_display = ('id', '__unicode__', 'last_login', 'is_verified', 'is_active', 'is_staff')
    list_display_links = ('__unicode__', )
    actions = [verify_user]
    formfield_overrides = {
        models.ManyToManyField: {'widget': admin.widgets.FilteredSelectMultiple(_("groups"), False)}
    }

    def get_form(self, request, obj=None, **kwargs):
        defaults = {}
        if obj is None:
            defaults['form'] = self.add_form
        defaults.update(kwargs)
        return super(MemberAdmin, self).get_form(request, obj, **defaults)


admin.site.register(Member, MemberAdmin)
