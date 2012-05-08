import datetime

from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm

class Itinerary(models.Model):
  users = models.ManyToManyField(User)
  name = models.CharField(max_length=255)
  created_on = models.DateTimeField(default=datetime.datetime.now, editable=False)
  start_date = models.DateField()
  end_date = models.DateField()

  def __unicode__(self):
    return self.name

class Event(models.Model):
  itinerary = models.ForeignKey(Itinerary)
  location = models.CharField(max_length=255)
  name = models.CharField(max_length=255)
  start_time = models.DateTimeField()
  end_time = models.DateTimeField()
  
  def __unicode__(self):
    return self.name



class ItineraryForm(ModelForm):
  class Meta:
    model = Itinerary

class EventForm(ModelForm):
  class Meta:
    model = Event
