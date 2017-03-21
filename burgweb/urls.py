"""burgweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from dashing.utils import router
from oscar.app import application
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
<<<<<<< HEAD
    url(r'^admin/login/?next=/admin/', application.urls),
    url(r'', include('portal.urls')),
=======
    #url(r'', include('portal.urls')),
>>>>>>> 8c006dd44a669043e48f060dfb68b2f9fe3ed4ba
    url(r'^dj/', include('dj.urls')),
    url(r'^dash/', include(router.urls)),
    url(r'^cal/', include('schedule.urls')),
    url(r'^rep/', include('reptrack.urls')),
    url(r'^clients/', include(application.urls)),
    url(r'^', include('cms.urls')),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

