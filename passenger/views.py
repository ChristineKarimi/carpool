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

def update_profile(request,username):
  user = User.objects.get(username = username)
  if request.method == 'POST':
    user_form = UserForm(request.POST, instance = request.user)
    profile_form = ProfileForm(request.POST, instance =request.user.passenger_profile, files = request.FILES)
    if user_form.is_valid() and profile_form.is_valid():
      print('gjhdgasjdg')
      user_form.save()
      profile_form.save()
      messages.success(request, ('Your profile was successfully updated!'))
      return redirect(reverse('passenger:profile', kwargs = {'username': request.user.username}))
    else:
      messages.error(request, ('Please correct the error below.'))

  else:
    user_form = UserForm(instance = request.user)
    profile_form = ProfileForm(instance = request.user.passenger_profile)
  return render(request, 'passengers/profiles/profile_form.html', {"user_form":user_form, "profile_form":profile_form})

@login_required
def profile(request, username):
  user = User.objects.get(username =username)
  if not user:
    return redirect('passenger')
  profiles = Passenger_profile.objects.get(user =user)

  title = f"{user.username}"

  return render(request, 'passengers/profiles/profile.html', {"title":title, "user":user, "profiles": profiles})
