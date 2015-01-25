from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mcexam.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('base.urls')),
    url(r'^admin/', include(admin.site.urls)),
)


if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += patterns('',
        url(r'^rosetta/', include('rosetta.urls')),
    )
