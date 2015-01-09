from django.db import models
from django.contrib.sites.models import Site

# Create your models here.


def site_details(request):
    return {
       'site': Site.objects.get_current(),
    }