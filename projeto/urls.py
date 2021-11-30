"""projeto URL Configuration

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
from django.urls import path
from app.views import create_espec, home, tab_clinica, tab_espec
from app.views import form_clinica, form_espec
from app.views import create_clinica, create_espec


urlpatterns = [
    path('admin/', admin.site.urls),
    #READ
    path('', home, name='home'),
    path('tab_clinica', tab_clinica, name='tab_clinica'),
    path('tab_espec', tab_espec, name='tab_espec'),
    #FORM
    path('form_clinica/', form_clinica, name='form_clinica'), 
    path('form_espec/', form_espec, name='form_espec'),
    #CREATE
    path('create_clinica', create_clinica, name='create_clinica'), 
    path('create_espec', create_espec, name='create_espec'),
]
