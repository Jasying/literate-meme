from django.conf.urls import url
from django.contrib import admin
from .views import (
    post_create,
	post_detail,
	post_list,
	post_update,
	post_delete,)
# this guides you to all things in urlpatterns

urlpatterns = [
    url(r'^create$', post_create),
    url(r'^(?P<id>\d+)$', post_detail, name='detail'),
    url(r'^$',post_list),
    url(r'^(?P<id>\d+)/edit/$', post_update, name='update'),
    url(r'^delete$', post_delete),
    # url(string, views.<function_name>),
]
