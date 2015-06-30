from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'songs.views.index', name='index'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^songs/', include('songs.urls', namespace="songs")),
    url(r'^feedback/', include('feedback.urls', namespace="feedback")),
    url(r'^may3/', include('dynamicmarathalli.urls', namespace="may3")),
    url(r'^contact/', 'songs.views.contact', name='contact'),
)
