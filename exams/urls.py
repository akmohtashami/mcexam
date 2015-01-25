from django.conf.urls import patterns, url

from exams import views

urlpatterns = patterns('',
                       url(r'^$', views.list, name='list'),
                       url(r'^exam/(?P<exam_id>\d+)/$', views.detail, name='detail'),
                       url(r'^exam/(?P<exam_id>\d+)/import/$', views.import_data, name='import'),
                       url(r'^exam/(?P<exam_id>\d+)/add_data/$', views.add_data, name='add_data'),
                       url(r'^exam/(?P<exam_id>\d+)/edit_data/(?P<user_id>\d+)/$', views.edit_data, name='edit_data'),
                       url(r'^exam/(?P<exam_id>\d+)/delete_data/(?P<user_id>\d+)/$', views.delete_data, name='delete_data'),
                       url(r'^exam/(?P<exam_id>\d+)/make_pdf/$', views.make_pdf),
                       url(r'^exam/(?P<exam_id>\d+)/make_tex/$', views.make_tex),
)
