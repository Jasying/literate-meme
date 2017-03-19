from django.conf.urls import url
from .views import (post_create,
	post_detail,
	post_list,
	post_update,
	post_delete,)
# this guides you to all things in urlpatterns

urlpatterns = [
    url(r'^create$', post_create),
    url(r'^detail$', post_detail),
    url(r'^$',post_list),
    url(r'^update$', post_update),
    url(r'^delete$', post_delete),
    # url(string, views.<function_name>),
]
