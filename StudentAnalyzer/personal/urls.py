from django.conf.urls import patterns,url
from . import views

urlpatterns = [
	url(r'^$', views.personalindex, name = 'personalindex')
]