from django.conf.urls import include, url
from django.contrib import admin
from .views import latest_post

urlpatterns = [
    url(r'^latest/', latest_post ),

]
