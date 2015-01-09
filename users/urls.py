from django.conf.urls import patterns, url

from exams import views

urlpatterns = patterns('',
                       url(r'^edit/$', 'users.views.edit_profile', name='edit_profile'),
                       url(r'^login/', 'users.views.login', name='login'),
                       url(r'^logout/', 'users.views.logout', name='logout'),
                       url(r'^register/', 'users.views.register', name='register'),
                       url(r'^verify/(?P<verification_code>.+)/', 'users.views.verify', name='verify'),
)
