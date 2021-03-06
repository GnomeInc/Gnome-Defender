"""
    Author: Eric Kuha
    File: views.py
    Project: Gnome Defender

    Copyright: GnomeInc, Some Rights Reserved
"""
from django.conf.urls import url
from django.contrib import admin
from django.http import HttpResponseRedirect
from django.conf.urls import include


urlpatterns = [
    url(r'^$', lambda r: HttpResponseRedirect('tracker/')),
    url(r'^tracker/', include('tracker.urls', namespace='tracker')),
    url(r'^admin/', include(admin.site.urls)),
]

# Set up Token Authentication Endpoint
from rest_framework.authtoken import views

urlpatterns += [
    url(r'^api-token-auth/', views.obtain_auth_token)
]