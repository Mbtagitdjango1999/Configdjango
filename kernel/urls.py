"""
URL configuration for kernel project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path
from django.conf import settings
from .settings.base import STATIC_URL,STATIC_ROOT,MEDIA_ROOT,MEDIA_URL
from decouple import config
from django.conf import global_settings
from .settings import base

urlpatterns = [
    path('admin/', admin.site.urls),
]
# + static(base.STATIC_URL, document_root=base.STATIC_ROOT)



#this is just for development area and ststic files

#in deploy area nginx do this part

if config("DEBUG_MODE",default = False,cast = bool):
    print("ffsdf")
    print(STATIC_URL)
    print(STATIC_ROOT)
    print(MEDIA_URL)
    print(MEDIA_ROOT)
    # urlpatterns += static(STATIC_URL,document_root = STATIC_ROOT)
    # urlpatterns += static(MEDIA_URL,document_root = MEDIA_ROOT)
    
    
    y = static(STATIC_URL,document_root = STATIC_ROOT)
    x =static(MEDIA_URL,document_root = MEDIA_ROOT)
    
    print(x, 'dsadd ;;' , y)
    
    urlpatterns += static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
    y = static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)
    x =static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
    print(x, 'dsadd ;;' , y)
    
    print(settings.STATIC_URL)
    print(settings.STATIC_ROOT)
    print(settings.MEDIA_URL)
    print(settings.MEDIA_ROOT)
    # urlpatterns += static('/static/',document_root = '/home/unobody/Desktop/1/media/collectstatic')
    # urlpatterns += static('/media/',document_root = 'media/')
    
    # generated__pic---ewzkOHHM.jpg