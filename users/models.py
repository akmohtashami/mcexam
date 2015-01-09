from django.db import models
from django.contrib import auth
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.sites.models import Site
from django.utils.translation import ugettext as _

import hashlib
import random

# Create your models here.


class MemberManager(auth.models.BaseUserManager):

    def create_user(self, username, email, first_name, last_name, first_name_en, last_name_en,
                    is_active, is_superuser, password):

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            first_name_en=first_name_en,
            last_name_en=last_name_en,
            is_active=is_active,
            is_superuser=is_superuser,
            )
        user.create_verification_code()
        user.send_verification_mail()
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, first_name, last_name, first_name_en, last_name_en, password):
        user = self.create_user(username, email, first_name, last_name, first_name_en, last_name_en, True, True, password)
        user.verify()
        user.is_admin = True
        user.save()
        return user


class Member(auth.models.AbstractBaseUser, auth.models.PermissionsMixin):
    username = models.CharField(max_length=200, unique=True, verbose_name=_("Username"))
    email = models.EmailField(max_length=255, unique=True, verbose_name=_("Email"))
    first_name = models.CharField(max_length=1000, verbose_name=_("First Name (Native)"))
    last_name = models.CharField(max_length=1000, verbose_name=_("Last Name (Native)"))
    first_name_en = models.CharField(max_length=1000, verbose_name=_("(First Name (English)"))
    last_name_en = models.CharField(max_length=1000, verbose_name=_("Last Name (English)"))
    is_active = models.BooleanField(default=True, verbose_name=_("Active"))

    verification_code = models.CharField(max_length=128, editable=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name', 'first_name_en', 'last_name_en']
    objects = MemberManager()

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __unicode__(self):
        return self.get_full_name()

    def get_full_name(self):
        return self.first_name + " " + self.last_name

    def get_short_name(self):
        return self.first_name[0] + ". " + self.last_name

    def create_verification_code(self):
        salt = hashlib.sha1("Th!siS@salT;,^%#WoW18s" + str(random.random())).hexdigest()
        self.verification_code = hashlib.sha1(salt[:10] + self.username + salt[10:]).hexdigest()

    def send_verification_mail(self):
        current_site = Site.objects.get_current()
        subject = render_to_string("users/activation_email_subject.txt", {"cur_user": self, "site": current_site})
        text = render_to_string("users/activation_email_text.txt", {"cur_user": self, "site": current_site})
        send_mail(subject, text, settings.EMAIL_SENDER, [self.email], False)

    def verify(self):
        self.verification_code = "verified"
        self.save()

    def is_verified(self):
        return self.verification_code == "verified"
    is_verified.short_description=_("Verified")
    is_verified.boolean = True

    def is_staff(self):
        return self.is_superuser
    is_staff.short_description=_("Staff")
    is_staff.boolean = True

    def has_perm(self, perm, obj=None):
        if not self.is_verified:
            return False
        return super(Member, self).has_perm(perm, obj)

    def has_module_perms(self, app_label):
        if not self.is_verified:
            return False
        return super(Member, self).has_module_perms(app_label)


