from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$', views.People.index, name='index'),
	url(r'^register/', views.People.register, name='register')
]