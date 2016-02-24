from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^add_gnome/$', login_required(views.AddGnomeView.as_view()), name='add_gnome'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^rest_tracker/$', views.DataSetSerializer.as_view(), name='rest_index')
]

# TODO Separate REST Service, I think.
