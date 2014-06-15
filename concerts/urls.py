from django.conf import settings
from django.conf.urls import patterns, include, url

from concerts import views

urlpatterns = patterns('',
  url( r'^concerts$', views.get_concerts, name='concerts' ),
  url( r'^artists$', views.get_artists, name='artists' )
)
