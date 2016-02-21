from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^tracker/', include('tracker.urls', namespace='tracker')),
    url(r'^admin/', include(admin.site.urls)),
]
