"""my_project URL Configuration
"""

from django.conf.urls import  url, include
# include means that you want to include your new url
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^posts/', include('posts.urls')),
    #url(string,include())
    #r represents string
    # ^ means if you match up to this point then you can look for posts
    # ^ = http://127.0.0.1:8000/
    # $ means end
    # in 'posts', we can find another url, inside that url, we can find the view
]
