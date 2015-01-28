from users.models import Member
from django.contrib.auth import backends


class MemberAuthBackend(backends.ModelBackend):

    def authenticate(self, username, password):
        try:
            user = Member.objects.get(username=username)
            if user.check_password(password):
                return user
            else:
                return None
        except Member.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Member.objects.get(pk=user_id)
        except Member.DoesNotExist:
            return None

