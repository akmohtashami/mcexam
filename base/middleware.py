import pytz

from django.utils import timezone


class TimeZoneMiddleware(object):

    def process_request(self, request):
        timezone.activate(pytz.timezone("Asia/Tehran"))
