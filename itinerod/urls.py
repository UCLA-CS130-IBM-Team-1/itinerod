from django.conf.urls import patterns, include, url
import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^itinerod/', include('itinerod.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
	
   (r'^$', include('registration.backends.default.urls')),
    (r'^$', 'django.contrib.auth.views.login',  {'template_name':'index.html'}),

    url(r'^google/login/$', 'django_openid_auth.views.login_begin', name='openid-login'),
    url(r'^google/login-complete/$', 'django_openid_auth.views.login_complete', name='openid-complete'),
    url(r'^google/$', 'django.contrib.auth.views.logout', {'next_page':'/'}, name='logout'),

    url(r'^$', 'itinerod.views.home', name='home'),
    url(r'^profile/$', 'itinerod.views.profile', name='profile'),
    url(r'^itinerary/(?P<itin_id>\d+)/$', 'itinerod.views.itinerary', name='itinerary'),


    # Media Files
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', 
      {'document_root' : settings.MEDIA_ROOT}),
)
