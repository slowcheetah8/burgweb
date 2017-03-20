from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^dj', views.index, name='index'),
]
