from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from .import views

app_name = 'passenger'

urlpatterns = [
  url(r'^$',views.passenger, name = 'passenger'),
  url(r'^profile/(?P<username>[-_\w.]+)/$', views.profile, name='profile'),
  url(r'^profile/(?P<username>[-_\w.]+)/edit/$', views.update_profile, name='edit'),
  url(r'^driver_profile/(\d+)/(\d+)/$', views.driver_profile, name='driver_profile'),
]
# if settings.DEBUG:
#   urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT )