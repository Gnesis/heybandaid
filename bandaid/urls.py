from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bandaid.views.home', name='home'),
    # url(r'^bandaid/', include('bandaid.foo.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url( r'^markitup/', include('markitup.urls') ),
    url( r'^api/', include('concerts.urls') ),
    url(r'^artist/', include('artists.urls')),
    url( r'^', include('users.urls') ),
)
