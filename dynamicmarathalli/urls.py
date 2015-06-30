from django.conf.urls import url, patterns
from dynamicmarathalli import views

urlpatterns = patterns('',
		url(r'^$', views.index, name='index'),
		url(r'^cultural/$', views.cultural_committee),
		url(r'^fd/$', views.fd_committee),
		url(r'^concept/$', views.concept_committee),
	)
