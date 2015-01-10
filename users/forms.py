from django import forms
from users.models import Member
from django.utils.translation import ugettext as _
from django.contrib.auth import authenticate
from django.utils.html import format_html


class ReadonlyWidget(forms.Widget):
    def render(self, name, value, attrs=None):
        return format_html("<input name='{0}' readonly value='{1}' />", name, value)


class ReadonlyField(forms.Field):
    widget = ReadonlyWidget


class FullMemberChangeForm(forms.ModelForm):

    password1 = forms.CharField(label=_('New Password'),
                                widget=forms.PasswordInput,
                                required=False,
                                help_text=_("Leave this empty if you don't want to change the password"))
    password2 = forms.CharField(label=_('New Password Confirmation'),
                                widget=forms.PasswordInput,
                                required=False)

    class Meta:
        model = Member
        fields = [
            'username',
            'email',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'first_name_en',
            'last_name_en',
            'school',
            'grade',
            ]

    def clean(self):
        super(FullMemberChangeForm, self).clean()
        if self.cleaned_data.get("password1") != self.cleaned_data.get("password2"):
            raise forms.ValidationError(_("Password Confirmation is not the same as Password"),
                                        code='password_not_confirmed')
        else:
            return self.cleaned_data

    def save(self, commit=True):
        user = super(FullMemberChangeForm, self).save(commit=False)
        if self.cleaned_data["password2"]:
            user.set_password(self.cleaned_data["password2"])
        if commit:
            user.save()
        return user


class RestrictedMemberChangeForm(FullMemberChangeForm):

    username = ReadonlyField(label=_("Username"))
    email = ReadonlyField(label=_("Email"))
    old_password = forms.CharField(label=_("Current password:"),
                                   widget=forms.PasswordInput,
                                   required=True,
                                   help_text=_("Enter your current password to confirm your changes"))

    class Meta:
        model = Member
        fields = [
            'username',
            'email',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'first_name_en',
            'last_name_en',
            'school',
            'grade',
            'old_password',
            ]

    def clean_username(self):
        return self.initial["username"]

    def clean_email(self):
        return self.initial["email"]

    def clean_old_password(self):
        if self.instance.check_password(self.cleaned_data["old_password"]):
            return self.cleaned_data["old_password"]
        else:
            raise forms.ValidationError(_("Your current password is not correct"), code='wrong_current_password')


class MemberRegisterForm(FullMemberChangeForm):

    password1 = forms.CharField(label=_('Password'),
                                widget=forms.PasswordInput,
                                )
    password2 = forms.CharField(label=_('Password Confirmation'),
                                widget=forms.PasswordInput,
                                )

    class Meta:
        model = Member
        fields = [
            'username',
            'email',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'first_name_en',
            'last_name_en',
            'school',
            'grade',
            ]

    def save(self, commit=True):
        user = super(MemberRegisterForm, self).save(commit=False)
        user.create_verification_code()
        user.send_verification_mail()
        user.set_password(self.cleaned_data["password2"])
        if commit:
            user.save()
        return user


class MemberAdminChangeForm(FullMemberChangeForm):
    is_active = forms.BooleanField(label=_("Active"),
                                   required=False,
    )

    class Meta:
        model = Member
        fields = [
            'username',
            'email',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'first_name_en',
            'last_name_en',
            'school',
            'grade',
            'is_active',
            'is_superuser',
            'groups',
            ]


class MemberAdminAddForm(FullMemberChangeForm):

    password1 = forms.CharField(label=_('Password'),
                                widget=forms.PasswordInput,
                                )
    password2 = forms.CharField(label=_('Password Confirmation'),
                                widget=forms.PasswordInput,
                                )
    is_active = forms.BooleanField(label=_("Active"), required=False, initial=True)

    class Meta:
        model = Member
        fields = [
            'username',
            'email',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'first_name_en',
            'last_name_en',
            'school',
            'grade',
            'is_active',
            'is_superuser',
        ]

    def save(self, commit=True):
        user = super(MemberAdminAddForm, self).save(commit=False)
        user.verify()
        user.set_password(self.cleaned_data["password2"])
        if commit:
            user.save()
        return user


class MemberLoginForm(forms.Form):

    username = forms.CharField(label=_("Username"))
    password = forms.CharField(label=_("Password"), widget=forms.PasswordInput)

    def clean(self):
        if self.cleaned_data.get("username") and self.cleaned_data.get("password"):
            user = authenticate(username=self.cleaned_data["username"], password=self.cleaned_data["password"])
            if user is None:
                raise forms.ValidationError(_("Provided username and password are not correct"), code='invalid_credentials')
            elif not user.is_active:
                raise forms.ValidationError(_("This user is deactivated by administrator."), code='deactivated_user')
            elif not user.is_verified():
                raise forms.ValidationError(_("This user is not verified. Please verify your user"),
                                            code='not_verified_user')
            else:
                return {"user": user}
        else:
            return self.cleaned_data

    def get_user(self):
        return self.cleaned_data["user"]


class MemberResendVerificationMailForm(forms.Form):
    email = forms.EmailField(label=_("Email"),
                             help_text=_("This must be the same email that you registered with"))

    def clean(self):
        if self.cleaned_data.get("email"):
            try:
                user = Member.objects.get(email=self.cleaned_data["email"])
                if user.is_verified():
                    raise forms.ValidationError(_("This user has been already verified"),
                                                code='already_verified')
            except Member.DoesNotExist:
                raise forms.ValidationError(_("No user is registered with this email address"),
                                            code='bad_email')
            return {"user": user}
        else:
            return self.cleaned_data

    def get_user(self):
        return self.cleaned_data["user"]