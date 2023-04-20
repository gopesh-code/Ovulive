"""PeriodsDateReminder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from home1 import execute
from django.urls import path
from home1.views import sender, email_temp
from home.views import home, add_form
from django.views.generic import TemplateView

urlpatterns = [
     path('admin/', admin.site.urls),
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type='text/plain')),
    path('', home, name="home"),
   
    path('add/', add_form, name="add_form"),
  
    path('sender/', sender, name="sender"),
    path('wish/<str:sender>/<str:receiver>/', email_temp, name="email_temp")
]
