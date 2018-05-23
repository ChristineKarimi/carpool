from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import UserForm,ProfileForm
from .models import Passenger_profile
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

# Create your views here.
def rider(request):
  user = User.objects.get(username = request.user.username)
  profile = Rider_profile.objects.get(user =user)
  return render(request, 'passengers/passenger.html')
