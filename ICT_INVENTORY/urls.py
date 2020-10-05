"""ICT_INVENTORY URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include
from users.views import IndexView
from land_admin import views

admin.site.site_header = "IMS Admin"
admin.site.site_title = "IMS Admin Portal"
admin.site.index_title = "Welcome to IMS Portal"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('', IndexView.as_view(), name= 'home'),
    path('landadmin/', include('land_admin.urls')),
    path('seventhfloor/', include('seventhfloor.urls')),
    path('bankinghall/', include('bankinghall.urls')),
    path('thirdfloor/', include('thirdfloor.urls')),
    path('fourthfloor/', include('fourthfloorwingA.urls')),
    path('tenthfloor/', include('tenthfloordataentry.urls')),
    path('scanners/', include('scanners.urls')),
    path('faulty/', include('faulty.urls')),
    path('messagingboard/', include('messagingboard.urls')),
    path('eighthfloor/', include('eighthfloor.urls')),
    path('groundfloor/', include('groundfloor.urls')),
    path('stockin/', include('stockin.urls')),
    path('landregistration/', include('landregistration.urls')),
    path('fifthfloor/', include('fifthfloor.urls')),
    path('ordereditem/', include('order.urls')),
















]
