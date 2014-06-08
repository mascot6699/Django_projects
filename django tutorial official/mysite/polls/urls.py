#!/usr/bin/env python
#this is under mysite/poll
from django.conf.urls import patterns, url

from polls import views
from polls.views import *

urlpatterns = patterns('',
    #url(r'^$', views.usindex, name='index'),                   
    url(r'^$', 											views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', 								views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/results/$', 						views.ResultsView.as_view(), name='results'),
    url(r'^(?P<poll_id>\d+)/vote/$', 					views.vote, name='vote'),
	url(r'^(?P<poll_id>\d+)/details1/$',                 mine),

)