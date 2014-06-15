from django.conf import settings
from django.conf.urls import patterns, include, url

from users import views

urlpatterns = patterns('',
	url( r'^$', views.index, name="index"),
	url( r'^signup/$', views.signup, name="signup"),
	url( r'^(?P<slug>[^\.]+)$', views.user, name="user"),
)