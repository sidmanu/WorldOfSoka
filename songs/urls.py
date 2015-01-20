from django.conf.urls import url, patterns
from songs import views

urlpatterns = patterns('',
		url(r'^$', views.index, name='index'),
		url(r'^download/(?P<song_id>\d+)/$', views.download, name='download'),
		url(r'^lang/(?P<lang>.+)/$', views.lang, name='lang'),
		url(r'^search/$', views.search, name='search'),
	)
