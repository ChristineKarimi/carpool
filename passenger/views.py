from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import UserForm,ProfileForm
from .models import Passenger_profile
# from drivers.models import Driver_profile,TripPlan,Booking
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.urlresolvers import reverse

# Create your views here.
def passenger(request):
  user = User.objects.get(username = request.user.username)
  profile = Passenger_profile.objects.get(user =user)
  drivers = Driver_profile.objects.all()
  return render(request, 'passenger/passenger.html', {"profile": profile, "drivers":drivers})
