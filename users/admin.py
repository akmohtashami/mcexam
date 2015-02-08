from django.contrib import admin
from django.contrib.auth.models import Group
from django.db import models
from users.models import Member
from users.forms import MemberAdminAddForm, MemberAdminChangeForm
from django.utils.translation import ugettext as _
from django.contrib.sites.models import Site
from django.template.loader import render_to_string
from django.utils.encoding import smart_text
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse



# Register your models here.

class MemberAdmin(admin.ModelAdmin):
    form = MemberAdminChangeForm
    add_form = MemberAdminAddForm
    list_display = ('id', '__unicode__', 'last_login', 'is_verified', 'is_active', 'is_staff', 'is_onsite')
    list_display_links = ('__unicode__', )
    list_filter = (
        ('groups__name'),
        ('exam_site'),
    )
    actions = ['verify_user', 'send_user_information', 'get_email_list']


    def verify_user(self, request, queryset):
        for user in queryset:
            user.verify()
            user.save()
    verify_user.short_description = _("Verify selected users")

    def send_user_information(self, request, queryset):
        current_site = Site.objects.get_current()
        for user in queryset:
            password = Member.objects.make_random_password()
            user.set_password(password)
            user.save()
            context = {"cur_user": user, "site": current_site, "cur_user_pass": password}
            subject = smart_text(render_to_string("users/user_info_email_subject.txt", context))
            text = smart_text(render_to_string("users/user_info_email_text.txt", context))
            send_mail(subject, text, settings.EMAIL_SENDER, [user.email], False)
    send_user_information.short_description = _("Send selected users info to their email")

    def get_email_list(self, request, queryset):
        emails = []
        for user in queryset:
            emails.append(user.email)
        return HttpResponse(", ".join(emails), content_type="text/plain")
    get_email_list.short_description = _("Get selected users email list")

    def get_form(self, request, obj=None, **kwargs):
        defaults = {}
        if obj is None:
            defaults['form'] = self.add_form
        defaults.update(kwargs)
        return super(MemberAdmin, self).get_form(request, obj, **defaults)


admin.site.register(Member, MemberAdmin)
