from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'gnome_defender.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^tracker', include('tracker.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
