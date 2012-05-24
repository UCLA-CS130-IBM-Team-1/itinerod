#Create your views here.
from settings import *
from models import *
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.template.loader import get_template
from django.core.paginator import Paginator
from django.core.context_processors import csrf
from django.forms.models import inlineformset_factory
from django.forms.formsets import formset_factory
from django.forms.models import modelformset_factory

from registration.forms import RegistrationForm

def home(request):
  '''
  if request.method == 'POST':
    print "post"
    registration_form = RegistrationForm(request.POST)
    if registration_form.is_valid():
      new_user = registration_form.save()
      return HttpResponseRedirect('/profile/') 
  else:
    print "not post"
  '''
  registration_form = RegistrationForm()

  print "out"

  t = get_template('index2.html')
  context = {
      'user' : request.user,
      'registration_form': registration_form,
      'login_form': AuthenticationForm(),
  }
  context.update(csrf(request))
  return render_to_response('index2.html',context)


@login_required
def profile(request):
  new_itinerary = Itinerary()
  if request.method == 'POST': # If the form has been submitted...
    form = ItineraryForm(request.POST, instance=new_itinerary) # A form bound to the POST data
    if form.is_valid(): #and event_set.is_valid(): # All validation rules pass # Process the data in form.cleaned_data
      new_itinerary = form.save()
      friends = form.cleaned_data['friends']   # Clean friends data sent by post (these are not included in the 'form' object and thus not saved).
      friendList = friends.split(',') # Parse the list of friends into tokens
      for x in friendList:
        try:
          u = User.objects.get(email=x); # If a friend exists in the system, get the user object
          new_itinerary.users.add(u.id)  # Create association between itinerary and friend
        except User.DoesNotExist:
          print("the user does not exist") # here we should consider the emailing ability to invite users.
      new_itinerary.users.add(request.user) # add the creator of the itinerary
      #event_set.save()
      return HttpResponseRedirect('/profile/') # Redirect after POST
  else:
    form = ItineraryForm() # An unbound form

  context = { 
      'page': 'profile',
      'form': form,
      'user': request.user,
      }
  context.update(csrf(request))

  return render_to_response('profile.html', context)

def voteCalc(event_set):
  for event in event_set:
	voteDeadline= event.vote_deadline
	# Take care of the case of null voteDeadlines
	if voteDeadline is None:
		voteDeadline = datetime.datetime.now()
	today = datetime.datetime.now()
	if voteDeadline < today:
		voteY = Vote.objects.filter(event=event.id,vote='Y')
		voteN = Vote.objects.filter(event=event.id,vote='N')
		if(voteY.count() >= voteN.count()):
			event.status = 'A'
		else:
			event.status = 'R'
		event.save()

def createEventList(event_set):
  event_list = []
  for event in event_set:
	if event.status == 'V':
		event_list.append(events)
  return event_list

@login_required
def itinerary(request, itin_id):
  # Primitively restricts access to itineraries to owners
  selected_itinerary = get_object_or_404(request.user.itinerary_set, pk=itin_id)
  itinEvents = Event.objects.filter(itinerary=itin_id)
  event_set = itinEvents.order_by('start_time')
  vote_set = Vote.objects;
  voteCalc(event_set)
  event_list = createEventList(event_set)

  VoteFormSet = formset_factory(VoteForm, extra=len(event_list))
  if request.method == 'POST':
    formset = VoteFormSet(request.POST)
    eventIndex = 0
    for form in formset:
	savedVoteForm = form.save(commit=False)
	savedVoteForm.user = request.user
	savedVoteForm.id = eventIndex+1
      	savedVoteForm.event = event_list[eventIndex]
	eventIndex+=1
    if formset.is_valid():
	for form in formset:
		savedVoteForm = form.save()
    else:
    	formset = VoteFormSet() # An unbound form
  context ={
	'itinerary' : selected_itinerary,
	'event_set' : event_set,
        'vote_set'  : vote_set,
	'vote_form_set' : VoteFormSet,
  }
  context.update(csrf(request))
  return render_to_response('itinerary.html',context)

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
