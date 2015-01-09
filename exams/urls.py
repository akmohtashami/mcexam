from django.conf.urls import patterns, url

from exams import views

urlpatterns = patterns('',
                       url(r'^$', views.list, name='list'),
                       url(r'^exam/(?P<exam_id>\d+)/$', views.detail, name='detail')
)
