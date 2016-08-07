from django.conf.urls import url,include
from feedback import views

urlpatterns = [
		url(r'^$', views.get_feedback, name='get_feedback'),
]
		
