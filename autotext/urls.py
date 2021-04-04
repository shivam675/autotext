"""autotext URL Configuration

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
from django.urls import path
from reminders import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name = 'home'),
    path('signupuser/', views.signupuser, name = 'signupuser'),
    path('loginuser/', views.loginuser, name = 'loginuser'),
    path('logoutuser/', views.logoutuser, name = 'logoutuser'),


    path('create_msg/', views.createmsgs, name = 'createmsgs'),
    path('current/', views.currentmsgs, name='currentmsgs'),
    path('completed/', views.completedmsgs, name='completedmsgs'),
    path('msg/<int:msg_pk>', views.viewmsgs, name='viewmsgs'),
    path('msg/<int:msg_pk>/complete', views.completemsgs, name='completemsgs'),
    path('msg/<int:msg_pk>/delete', views.deletemsgs, name='deletemsgs'),
]
