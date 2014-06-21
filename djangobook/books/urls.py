from django.conf.urls import patterns, include, url
from books.views import *


urlpatterns = patterns('',
(r'^search/$', search),
(r'^contact/$', contact),

)

