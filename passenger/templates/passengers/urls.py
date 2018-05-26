from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from .import views

app_name = 'passenger'

urlpatterns = [
  url(r'^$',views.passenger, name = 'passenger'),

]