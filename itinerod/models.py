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

EVENT_STATUS_CHOICES = (
    ('V', 'Vote in Progress'),
    ('A', 'Approved'),
    ('R', 'Rejected'),
    ('D', 'Deleted'),
)

class Event(models.Model):
  name = models.CharField(max_length=255)
  itinerary = models.ForeignKey(Itinerary)
  location = models.CharField(max_length=255)
  start_time = models.DateTimeField()
  end_time = models.DateTimeField()
  status = models.CharField(max_length=1, choices=EVENT_STATUS_CHOICES)
  vote_deadline = models.DateTimeField(null=True, blank=True)
  
  def __unicode__(self):
    return self.name

VOTE_CHOICES = (
    ('Y', 'Yes'),
    ('N', 'No'),
    ('A', 'Abstain'),
)

class Vote(models.Model):
  user = models.ForeignKey(User)
  event = models.ForeignKey(Event)
  vote = models.CharField(max_length=1, choices=VOTE_CHOICES)

  def __unicode__(self):
    return 'Vote:%s, %s' % (self.user.username, self.event.name,)

class ItineraryForm(ModelForm):
  friends = CharField(label='Travel Buddies', required=False, help_text = "enter Travel Buddies' emails, separate by commas") # This is the friends field in the form
  class Meta:
    model = Itinerary
    fields = ('friends','name', 'start_date', 'end_date') #Friends was added to appear
  def __init__(self, *args, **kwargs):
    super(ItineraryForm, self).__init__(*args, **kwargs)
    self.fields['start_date'].widget = extras.widgets.SelectDateWidget()
    self.fields['end_date'].widget = extras.widgets.SelectDateWidget()

class EventForm(ModelForm):
  class Meta:
    model = Event
  def __init__(self, *args, **kwargs):
    super(EventForm, self).__init__(*args, **kwargs)
    #self.fields['start_time'].widget = widgets.SplitDateTimeWidget()
    #self.fields['end_time'].widget = widgets.SplitDateTimeWidget()
    #self.fields['approval_status'].widget.choices = ()
    #self.fields['approval_status'].choices = (('V', 'Votable'))
