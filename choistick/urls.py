from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'choistick'
urlpatterns = [
	path('', views.index, name='index'),
	path('map/', views.map, name='map'),
	path('join/', views.signup, name='join'),
	path('pick/', views.pick, name='pick'),
	path('warn/', views.warn, name='warn'),
	# url(r'^login/$', views.signin, name='login'),
	url(r'^login/$', views.signin, name='login'),
]