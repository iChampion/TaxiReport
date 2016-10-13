# coding: utf-8
from django.conf.urls import url

from . import views

# urlpatterns = patterns('',
#
#                        url(r'^login/$', 'weblogin.views.login'),
#                        url(r'^logout/$', 'weblogin.views.logout'),
#                        url(r'^$', 'weblogin.views.login'),
# )
urlpatterns = [

    url(r'^login/$', views.login, name="login"),
    url(r'^logout/$', views.logout, name="logout"),
    url(r'^$', views.login, name="login"),
]