from django.conf.urls import patterns, url
from itcastsubject import views


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^showsubject/(?P<Subject_name_slug>[\w\-]+)/$', views.showsubject,name='showsubject'),# New!
    url(r'^add_subject/$', views.add_subject, name='add_subject'),
    url(r'^subject/(?P<subject_name_slug>[\w\-]+)/add_page/$', views.add_page, name='add_page'),

)  
