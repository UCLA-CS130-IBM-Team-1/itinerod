import datetime

from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm, widgets, extras, Textarea, CharField, ModelMultipleChoiceField
import django.forms

class Itinerary(models.Model):
  users = models.ManyToManyField(User)
  name = models.CharField(max_length=255)
  created_on = models.DateTimeField(default=datetime.datetime.now, editable=False)
  start_date = models.DateField()
  end_date = models.DateField()

  def __unicode__(self):
    return self.name

class Location(models.Model):
  itinerary = models.ForeignKey(Itinerary)
  name = models.CharField(max_length=255)
  start_time = models.DateTimeField()
  end_time = models.DateTimeField()

  def __unicode__(self):
    return self.name

class Event(models.Model):
  location = models.ForeignKey(Location)
  name = models.CharField(max_length=255)
  start_time = models.DateTimeField()
  end_time = models.DateTimeField()
  
  def __unicode__(self):
    return self.name



class ItineraryForm(ModelForm):
  friends = CharField(label='Travel Buddies', help_text = "enter Travel Buddies' emails, separate by commas") # This is the friends field in the form
  class Meta:
    model = Itinerary
    fields = ('friends','name', 'start_date', 'end_date') #Friends was added to appear
  def __init__(self, *args, **kwargs):
    super(ItineraryForm, self).__init__(*args, **kwargs)
    self.fields['start_date'].widget = extras.widgets.SelectDateWidget()
    self.fields['end_date'].widget = extras.widgets.SelectDateWidget()

class LocationForm(ModelForm):
  class Meta:
    model = Location 
  def __init__(self, *args, **kwargs):
    super(LocationForm, self).__init__(*args, **kwargs)
    self.fields['start_time'].widget = widgets.SplitDateTimeWidget()
    self.fields['end_time'].widget = widgets.SplitDateTimeWidget()

class EventForm(ModelForm):
  class Meta:
    model = Event
  def __init__(self, *args, **kwargs):
    super(EventForm, self).__init__(*args, **kwargs)
    self.fields['start_time'].widget = widgets.SplitDateTimeWidget()
    self.fields['end_time'].widget = widgets.SplitDateTimeWidget()
