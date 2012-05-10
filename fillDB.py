from itinerod.models import Itinerary, Location
from django.contrib.auth.models import User

u = User.objects.all()
up = u[0]

# fill itinerary table
it1=up.itinerary_set.create(name="funtrip", start_date="2011-01-01", end_date="2011-02-02")
it2=up.itinerary_set.create(name="secondtrip", start_date="2012-03-01", end_date="2012-04-02")

# fill location table
l1 = it1.location_set.create(name='LA', start_time='2011-01-01', end_time='2011-01-15')
l2 = it1.location_set.create(name='SF', start_time='2011-01-15', end_time='2011-02-02')
l3 = it2.location_set.create(name='NY', start_time='2012-03-01', end_time='2012-04-02')

# fill activity table
l1.event_set.create(name="hollywood blvd", start_time="2012-01-01", end_time="2012-01-02")
l1.event_set.create(name="westwood LA", start_time="2012-01-02", end_time="2012-01-03")
l2.event_set.create(name="sf bay", start_time="2012-01-15", end_time="2012-01-16")
