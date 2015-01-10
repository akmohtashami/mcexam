from django.shortcuts import render
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from users.forms import RestrictedMemberChangeForm, MemberLoginForm, MemberRegisterForm, MemberResendVerificationMailForm
from users.models import Member
from django.http import HttpResponseRedirect
from django.utils.http import is_safe_url
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _


# Create your views here.

@login_required
def edit_profile(request):
    current_user = Member.objects.get(pk=request.user.id)
    if request.method == "POST":
        form = RestrictedMemberChangeForm(request.POST, instance=current_user)
        if form.is_valid():
            form.save()
            auth.update_session_auth_hash(request, current_user)
            request.user = current_user
            messages.success(request, _("Your profile has been updated successfully"))
    else:
        form = RestrictedMemberChangeForm(instance=current_user)

    return render(request, "users/edit_profile.html", {"form": form})


def get_next_page(request, default_redirect=reverse("index")):
    redirect_to = request.POST.get("next",
                                   request.GET.get("next", default_redirect))
    if not is_safe_url(redirect_to, request.get_host()):
        redirect_to = default_redirect
    return redirect_to


def login(request):
    redirect_to = get_next_page(request)
    if request.user.is_authenticated():
        return HttpResponseRedirect(redirect_to)
    if request.method == "POST" and 'login_button' in request.POST:
        login_form = MemberLoginForm(request.POST, prefix="login")

        if login_form.is_valid():
            auth.login(request, login_form.get_user())
            messages.success(request, _("You have successfully logged in"))
            return HttpResponseRedirect(redirect_to)
    else:
        login_form = MemberLoginForm(prefix="login")

    if request.method == "POST" and 'resend_verification_mail_button' in request.POST:
        resend_form = MemberResendVerificationMailForm(request.POST, prefix="resend")
        if resend_form.is_valid():
            resend_form.get_user().send_verification_mail()
            messages.success(request, _("A new verification mail has been sent to your email address"))
            resend_form = MemberResendVerificationMailForm(prefix="resend")
    else:
        resend_form = MemberResendVerificationMailForm(prefix="resend")

    return render(request, "users/login.html", {"login_form": login_form,
                                                "resend_verification_mail_form": resend_form})


def logout(request):
    redirect_to = get_next_page(request)

    auth.logout(request)
    messages.success(request, _("You have successfully logged out"))
    return HttpResponseRedirect(redirect_to)


def register(request):
    redirect_to = reverse("index")

    if request.user.is_authenticated():
        return HttpResponseRedirect(redirect_to)
    elif request.method=="POST":
        form = MemberRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "users/register_success.html")
    else:
        form = MemberRegisterForm()
    return render(request, "users/register.html", {"form": form})


def verify(request, verification_code):
    try:
        user = Member.objects.get(verification_code=verification_code)
        user.verify()
        messages.success(request, _("Your user has been verified. You can now login using the login form."))
    except Member.DoesNotExist:
        messages.error(request, _("Invalid verification code"))
    return HttpResponseRedirect(reverse("index"))