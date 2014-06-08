from django.conf.urls import patterns, include, url
from views import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
(r'^time/$', current_datetime),
(r'^time/plus/(\d{1,2})/$', hours_ahead),
(r'^time/minus/(\d{1,2})/$', hours_behind),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
