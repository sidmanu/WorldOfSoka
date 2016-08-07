from django.contrib import admin
from django.conf.urls import url,include
from songs import views

urlpatterns = [ 
    # Examples:
    url(r'^$', views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^songs/', include('songs.urls', namespace="songs")),
    url(r'^feedback/', include('feedback.urls', namespace="feedback")),
    url(r'^contact/', views.contact, name='contact'),
]

