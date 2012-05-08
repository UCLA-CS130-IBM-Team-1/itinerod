#Create your views here.
from settings import *
from models import *
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.loader import get_template
from django.core.paginator import Paginator
from django.core.context_processors import csrf

def home(request):
  if request.method == 'POST': # If the form has been submitted...
    form = ItineraryForm(request.POST) # A form bound to the POST data
    if form.is_valid(): # All validation rules pass # Process the data in form.cleaned_data
      form.save()
      return HttpResponseRedirect('/') # Redirect after POST
    print "form not vaild"
  else:
    form = ItineraryForm() # An unbound form
  t = get_template('index.html')
  context = { 
      'page': 'home',
      'form': form,
      }
  context.update(csrf(request))
      
  return render_to_response('index.html', context)

'''
def home(request):
  t = get_template('index.html')
  context = { 
      'page': 'home',
      'form': ItineraryForm()
      }
  html = t.render(RequestContext(request, context))
  return HttpResponse(html)
  '''

@login_required
def profile(request):
  t = get_template('profile.html')
  context = { 'page': 'profile'}
  html = t.render(RequestContext(request, context))
  return HttpResponse(html)

@login_required
def itinerary(request):
  t = get_template('itinerary.html')
  context = { 'page': 'itinerary'}
  html = t.render(RequestContext(request, context))
  return HttpResponse(html)

'''
def add_itinerary(request):
   
  if request.method == 'POST':
    new_itin = Itinerary()
    form = ItineraryForm(request.POST, instance=new_itin)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect('/itinerary/%s/' % new_itin.id)
      '''
