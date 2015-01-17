from django.conf.urls import url, patterns
from feedback import views

urlpatterns = patterns('',
		url(r'^$', views.get_feedback, name='get_feedback'),
	)
		
