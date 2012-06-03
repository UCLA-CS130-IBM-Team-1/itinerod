from django.conf.urls import patterns, include, url
from tastypie.api import Api
import settings
from api import *

from django.contrib import admin
admin.autodiscover()

itinerod_api = Api(api_name='itinerod')
itinerod_api.register(UserResource())
itinerod_api.register(ItineraryResource())
itinerod_api.register(EventResource())
itinerod_api.register(VoteResource())
itinerod_api.register(EventCommentResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^itinerod/', include('itinerod.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^api/leave_itinerary/(?P<itin_id>\d+)/$', 'itinerod.views.leave_itinerary', name='leave_itinerary'),
    url(r'^api/delete_friend/(?P<itin_id>\d+)/(?P<friend_id>\d+)$','itinerod.views.delete_friend',name='delete_friend'),
    url(r'^api/voted/(?P<itin_id>\d+)/(?P<event_id>\d+)/(?P<vote>\d+)$','itinerod.views.voted',name='voted'),
    url(r'^api/', include(itinerod_api.urls)),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
	
    url(r'^$', 'itinerod.views.home', name='home'),
    url(r'^accounts/', include('registration.backends.default.urls')),

    url(r'^google/login/$', 'django_openid_auth.views.login_begin', name='openid-login'),
    url(r'^google/login-complete/$', 'django_openid_auth.views.login_complete', name='openid-complete'),
    url(r'^google/$', 'django.contrib.auth.views.logout', {'next_page':'/'}, name='logout'),

    url(r'^profile/$', 'itinerod.views.profile', name='profile'),
    url(r'^itinerary/(?P<itin_id>\d+)/$', 'itinerod.views.itinerary', name='itinerary'),


    # Media Files
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', 
      {'document_root' : settings.MEDIA_ROOT}),

)
