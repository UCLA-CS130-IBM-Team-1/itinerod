from django.contrib.auth.models import User
from tastypie import fields, utils
from tastypie.resources import ModelResource
from tastypie.authentication import Authentication, BasicAuthentication, OAuthAuthentication
from tastypie.authorization import DjangoAuthorization
from tastypie.constants import ALL_WITH_RELATIONS
from models import *

import sys



class UserResource(ModelResource):
  itineraries = fields.ToManyField('itinerod.api.ItineraryResource', 'itinerary_set', related_name='user')
  class Meta:
    queryset = User.objects.all()
    fields = ['username', 'first_name', 'last_name', 'email', 'date_jonined']
    allowed_methods = ['get']
    authentication = Authentication()
    authorization = DjangoAuthorization()
  def obj_create(self, bundle, request=None, **kwargs):
    return super(UserResource, self).obj_create(bundle, request, user=request.user)

  def apply_authorization_limits(self, request, object_list):
    if request.user.is_anonymous():
      return object_list.none()
    else:
      return object_list.filter(pk=request.user.pk)

class ItineraryResource(ModelResource):
  users = fields.ToManyField(UserResource, 'users', related_name='itinerary')
  events = fields.ToManyField('itinerod.api.EventResource', 'event_set', related_name='itinerary')
  class Meta:
    queryset = Itinerary.objects.all()
    authentication = Authentication()
    authorization = DjangoAuthorization()
    filtering = {
        'name': ['exact'],
        'created_on': ['exact', 'range', 'gt', 'lt', 'lte'],
        'start_date': ['exact', 'range', 'gt', 'lt', 'lte'],
        'end_date': ['exact', 'range', 'gt', 'lt', 'lte'],
    }
    ordering = ['created_on', 'start_date', 'end_date']

  def obj_create(self, bundle, request=None, **kwargs):
    return super(ItineraryResource, self).obj_create(bundle, request, user=request.user)

  def apply_authorization_limits(self, request, object_list):
    if request.user.is_anonymous():
      return object_list.none()
    else:
      #return request.user.itinerary_set.all()
      return object_list.filter(users__pk=request.user.pk)

class EventResource(ModelResource):
  class Meta:
    queryset = Event.objects.all()
    authentication = Authentication()
    authorization = DjangoAuthorization()
    filtering = {
        'name': ['exact'],
        'itinerary': ALL_WITH_RELATIONS,
        'location': ['exact', 'startswith'],
        'start_date': ['exact', 'range', 'gt', 'lt', 'lte'],
        'end_date': ['exact', 'range', 'gt', 'lt', 'lte'],
        'status': ['exact'],
    }
    ordering = ['created_on', 'start_date', 'end_date', 'location', 'name', 'status']

  def obj_create(self, bundle, request=None, **kwargs):
    return super(EventResource, self).obj_create(bundle, request, user=request.user)

  def apply_authorization_limits(self, request, object_list):
    return object_list.filter(itinerary__users__pk=request.user.pk)


class VoteResource(ModelResource):
  class Meta:
    queryset = Vote.objects.all()
    authentication = Authentication()
    authorization = DjangoAuthorization()

  def obj_create(self, bundle, request=None, **kwargs):
    return super(VoteResource, self).obj_create(bundle, request, user=request.user)

  def apply_authorization_limits(self, request, object_list):
    return object_list.filter(user=request.user)