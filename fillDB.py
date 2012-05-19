from itinerod.models import Itinerary
from django.contrib.auth.models import User


for u in User.objects.all():

  # fill itinerary table
  it1=u.itinerary_set.create(name="California", start_date="2011-01-01", end_date="2011-02-02")
  it2=u.itinerary_set.create(name="New York", start_date="2012-03-01", end_date="2012-04-02")

  # fill activity table
  it1.event_set.create(name="Chinese Theater", start_time="2012-01-01", end_time="2012-01-02", location='Hollywood', status='V', vote_deadline='2012-05-20T00:00:00')
  it1.event_set.create(name="UCLA", start_time="2012-01-02", end_time="2012-01-03", location='Westwood', status='A')
  it1.event_set.create(name="Golden Gate Bridge", start_time="2012-01-15", end_time="2012-01-16", location='San Francisco', status='R')

  # fill activity table
  it2.event_set.create(name="Statue of Liberty", start_time="2012-01-01", end_time="2012-01-02", location='New York', status='V', vote_deadline='2012-05-20T00:00:00')
  it2.event_set.create(name="Times Square", start_time="2012-01-02", end_time="2012-01-03", location='New York', status='V')
  it2.event_set.create(name="Freedom Tower", start_time="2012-01-15", end_time="2012-01-16", location='New York', status='D')
