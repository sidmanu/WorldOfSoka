from django.contrib import admin
from django.conf.urls import url,include
from rest_framework import generics
from songs.models import Song 
from songs.serializers import SongSerializer

from songs import views

urlpatterns = [ 
		url(r'^$', views.index, name='index'),
		url(r'^rest/$', views.SongView.as_view(), name='song-list'),
		url(r'^rest/lang/(?P<lang_name>.+)/$', views.LangView().as_view(), name='lang-based-song-list'),
		url(r'^download/(?P<song_id>\d+)/$', views.download, name='download'),
		url(r'^lang/(?P<lang>.+)/$', views.lang, name='lang'),
		url(r'^search/$', views.search, name='search'),
		url(r'^tag/(?P<tag>.+)/$', views.tag),
		url(r'^update_lyrics/$', views.update_lyrics, name='update_lyrics'),
]
