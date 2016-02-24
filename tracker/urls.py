"""
    Author: Eric Kuha
    File: views.py
    Project: Gnome Defender

    Copyright: GnomeInc, Some Rights Reserved
"""
from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^add_gnome/$', login_required(views.AddGnomeView.as_view()), name='add_gnome'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^rest_index/$', views.DataSetList.as_view(), name='rest_index'),
    url(r'^rest_users/$', views.UserList.as_view(), name='rest_user_index'),
    url(r'^rest_users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='rest_user_detail'),
    url(r'^rest_gnomes/$', views.GnomeList.as_view(), name='rest_gnome_index'),
    url(r'^rest_gnomes/(?P<pk>[0-9]+)/$', views.GnomeDetail.as_view(), name='rest_gnome_detail'),
]
