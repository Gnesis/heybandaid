from django.conf import settings
from django.conf.urls import patterns, include, url

from artists import views

urlpatterns = patterns('',
	url( r'^signup/$', views.signup, name="signup"),
	url( r'^add-concert/$', views.add_concert, name="add_concert"),
	url( r'^(?P<slug>[^\.]+)$', views.artist, name="artist"),
)