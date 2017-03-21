from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^cal/', include('schedule.urls')),
    url(r'^rep/', include('reptrack.urls')),
]
