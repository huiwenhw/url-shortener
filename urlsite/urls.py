from django.conf.urls import include, url

from . import views

urlpatterns = [
	url(r'^$', views.HomeView.as_view(), name='home'),
	url(r'^shorturl/$', views.short_url, name='short_url'),
	# should be a regex consisting shorturl
	url(r'^[a-zA-Z0-9]+$', views.redirect_long, name='redirect_long'),
]