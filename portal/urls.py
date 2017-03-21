from django.conf.urls import url, include
from . import views
from schedule import urls

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^cal/', include('schedule.urls')),
    url(r'^')
]
