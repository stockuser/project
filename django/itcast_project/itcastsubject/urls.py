# itcastsubject/urls.py

from django.conf.urls import patterns, url
from itcastsubject import views
urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       # New!
                       url(r'^showsubject/(?P<Subject_name_slug>[\w\-]+)/$',
                           views.showsubject, name='showsubject'),
                       url(r'^add_subject/$', views.add_subject,
                           name='add_subject'),
                       url(r'^subject/(?P<subject_name_slug>[\w\-]+)/add_page/$',
                           views.add_page, name='add_page'),
                       url(r'^register/$', views.register, name='register'),
                       url(r'^restricted/$', views.restricted, name='restricted'),
                       url(r'^login/$', views.user_login, name='login'),
                       url(r'^logout/$',views.user_logout,name='logout'),
                       )
