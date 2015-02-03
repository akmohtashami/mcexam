from django.conf.urls import patterns, url

from exams import views

urlpatterns = patterns('',
                       url(r'^$', views.main_views.list, name='list'),
                       url(r'^exam/(?P<exam_id>\d+)/$', views.main_views.detail, name='detail'),
                       url(r'^exam/(?P<exam_id>\d+)/answer_sheet/$', views.contestant_views.answer_sheet, name='answer_sheet'),
                       url(r'^exam/(?P<exam_id>\d+)/import_panel/$', views.importer_views.import_panel, name='import_panel'),
                       url(r'^exam/(?P<exam_id>\d+)/add_data/$', views.importer_views.add_data, name='add_data'),
                       url(r'^exam/(?P<exam_id>\d+)/edit_data/(?P<user_id>\d+)/$', views.importer_views.edit_data, name='edit_data'),
                       url(r'^exam/(?P<exam_id>\d+)/delete_data/(?P<user_id>\d+)/$', views.importer_views.delete_data, name='delete_data'),
                       url(r'^exam/(?P<exam_id>\d+)/make_pdf/$', views.admin_views.preview_statements, name='preview_statements'),
                       url(r'^exam/(?P<exam_id>\d+)/make_tex/$', views.admin_views.show_statements_tex, name='show_statements_tex'),
                       url(r'^exam/(?P<exam_id>\d+)/publish_statements/$', views.admin_views.publish_statements, name='publish_statements'),
                       url(r'^exam/(?P<exam_id>\d+)/statements/$', views.contestant_views.statements, name='statements'),

)
