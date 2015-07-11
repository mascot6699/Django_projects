from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<blog_id>[0-9]+)/$', views.blogname, name='name'),
]