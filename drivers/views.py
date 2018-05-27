from django.contrib.auth.decorators import login_required
from .forms import UserForm, DriverProfileForm,TripPlanForm
from .models import Driver_profile,TripPlan
from passenger.models import Passenger_profile
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.db import transaction

# Create your views here.
def driver(request):
  user = User.objects.get(username = request.user.username)
  profile = Driver_profile.objects.get(user =user)
  passengers = Passenger_profile.objects.all()
  if request.method == 'POST':
    trip_form = TripPlanForm(request.POST)
    if trip_form.is_valid():
      trip_plan= TripPlan(driver_profile = request.user.driver_profile, current_location = request.POST['current_location'],destination = request.POST['destination'])
      trip_plan.save()
      print('success')
      return redirect(reverse('drivers:driver'))
  else:
    trip_form = TripPlanForm()
  return render(request, 'driver/driver.html',{"profile": profile, "passengers": passengers, "trip_form":trip_form})

