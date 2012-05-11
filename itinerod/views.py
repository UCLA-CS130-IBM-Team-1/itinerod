#Create your views here.
from settings import *
from models import *
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.template.loader import get_template
from django.core.paginator import Paginator
from django.core.context_processors import csrf
from django.forms.models import inlineformset_factory

def home(request):
  t = get_template('index.html')
  context = { 
      'page': 'home',
      }
  html = t.render(RequestContext(request, context))
  return HttpResponse(html)

@login_required
def profile(request):
  new_itinerary = Itinerary()
  #LocationFormSet = inlineformset_factory(Itinerary, Location)
  if request.method == 'POST': # If the form has been submitted...
    form = ItineraryForm(request.POST, instance=new_itinerary) # A form bound to the POST data
    #location_set = LocationFormSet(request.POST, instance=new_itinerary)
    if form.is_valid(): #and event_set.is_valid(): # All validation rules pass # Process the data in form.cleaned_data
      new_itinerary = form.save()
      new_itinerary.users.add(request.user)
      #event_set.save()
      return HttpResponseRedirect('/profile/') # Redirect after POST
    print "form not vaild"
  else:
    form = ItineraryForm() # An unbound form
    #location_set = LocationFormSet(instance=new_itinerary)

  #t = get_template('index.html')


  context = { 
      'page': 'profile',
      'form': form,
      #'location_set': location_set,
      'user': request.user,
      }
  context.update(csrf(request))
      
  return render_to_response('profile.html', context)


@login_required
def itinerary(request, itin_id):

  # Primitively restricts access to itineraries to owners
  selected_itinerary = get_object_or_404(request.user.itinerary_set, pk=itin_id)

  return render_to_response('itinerary.html', {'itinerary' : selected_itinerary })

'''
def itinerary(request):
  t = get_template('itinerary.html')
  context = { 'page': 'itinerary'}
  html = t.render(RequestContext(request, context))
  return HttpResponse(html)
  '''

'''
def add_itinerary(request):
   
  if request.method == 'POST':
    new_itin = Itinerary()
    form = ItineraryForm(request.POST, instance=new_itin)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect('/itinerary/%s/' % new_itin.id)
      '''
