from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView
from base import views

urlpatterns = patterns('',
    url(r'^profile/', include('users.urls', namespace="users")),
    url(r'^exams/', include('exams.urls', namespace="exams")),
    url(r'^$', views.index, name="index"),
)