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
from app.views import home, tab_clinica, tab_espec, tab_med, tab_pac, tab_agenda, tab_climed
from app.views import form_clinica, form_espec, form_med, form_pac, form_agenda, form_climed
from app.views import view_clinica, view_espec, view_pac, view_med, view_agenda, view_climed
from app.views import create_clinica, create_espec, create_med, create_pac, create_agenda, create_climed
from app.views import edit_clinica, edit_espec, edit_pac, edit_med, edit_agenda, edit_climed
from app.views import update_clinica, update_espec, update_pac, update_med, update_agenda, update_climed
from app.views import delete_clinica, delete_espec, delete_med, delete_pac, delete_agenda, delete_climed
from app.views import delete_all_clinica, delete_all_espec, delete_all_med, delete_all_pac, delete_all_agenda, delete_all_climed

urlpatterns = [
    path('admin/', admin.site.urls),
    # READ------------------------------------------------------------------------
    path('', home, name='home'),
    path('tab_clinica/', tab_clinica, name='tab_clinica'),
    path('tab_espec/', tab_espec, name='tab_espec'),
    path('tab_med/', tab_med, name='tab_med'),
    path('tab_pac/', tab_pac, name='tab_pac'),
    path('tab_agenda/', tab_agenda, name='tab_agenda'),
    path('tab_climed/', tab_climed, name='tab_climed'),
    # FORM------------------------------------------------------------------------
    path('form_clinica/', form_clinica, name='form_clinica'),
    path('form_espec/', form_espec, name='form_espec'),
    path('form_med/', form_med, name='form_med'),
    path('form_pac/', form_pac, name='form_pac'),
    path('form_agenda/', form_agenda, name='form_agenda'),
    path('form_climed/', form_climed, name='form_climed'),
    # CREATE------------------------------------------------------------------------
    path('create_clinica/', create_clinica, name='create_clinica'),
    path('create_espec/', create_espec, name='create_espec'),
    path('create_med/', create_med, name='create_med'),
    path('create_pac/', create_pac, name='create_pac'),
    path('create_agenda/', create_agenda, name='create_agenda'),
    path('create_climed/', create_climed, name='create_climed'),
    # VIEW------------------------------------------------------------------------
    path('view_clinica/<int:pk>/', view_clinica, name='view_clinica'),
    path('view_espec/<int:pk>/', view_espec, name='view_espec'),
    path('view_pac/<int:pk>/', view_pac, name='view_pac'),
    path('view_med/<int:pk>/', view_med, name='view_med'),
    path('view_agenda/<int:pk>/', view_agenda, name='view_agenda'),
    path('view_climed/<int:pk>/', view_climed, name='view_climed'),
    # EDIT------------------------------------------------------------------------
    path('edit_clinica/<int:pk>/', edit_clinica, name='edit_clinica'),
    path('edit_espec/<int:pk>/', edit_espec, name='edit_espec'),
    path('edit_pac/<int:pk>/', edit_pac, name='edit_pac'),
    path('edit_med/<int:pk>/', edit_med, name='edit_med'),
    path('edit_agenda/<int:pk>/', edit_agenda, name='edit_agenda'),
    path('edit_climed/<int:pk>/', edit_climed, name='edit_climed'),
    # UPDATE------------------------------------------------------------------------
    path('update_clinica/<int:pk>/', update_clinica, name='update_clinica'),
    path('update_espec/<int:pk>/', update_espec, name='update_espec'),
    path('update_pac/<int:pk>/', update_pac, name='update_pac'),
    path('update_med/<int:pk>/', update_med, name='update_med'),
    path('update_agenda/<int:pk>/', update_agenda, name='update_agenda'),
    path('update_climed/<int:pk>/', update_climed, name='update_climed'),
    # DELETE-------------------------------------------------------------------------
    path('delete_clinica/<int:pk>/', delete_clinica, name='delete_clinica'),
    path('delete_espec/<int:pk>/', delete_espec, name='delete_espec'),
    path('delete_med/<int:pk>/', delete_med, name='delete_med'),
    path('delete_pac/<int:pk>/', delete_pac, name='delete_pac'),
    path('delete_agenda/<int:pk>/', delete_agenda, name='delete_agenda'),
    path('delete_climed/<int:pk>/', delete_climed, name='delete_climed'),
    # DELETE ALL--------------------------------------------------------------------
    path('delete_all_clinica/', delete_all_clinica, name='delete_all_clinica'),
    path('delete_all_espec/', delete_all_espec, name='delete_all_espec'),
    path('delete_all_med/', delete_all_med, name='delete_all_med'),
    path('delete_all_pac/', delete_all_pac, name='delete_all_pac'),
    path('delete_all_agenda/', delete_all_agenda, name='delete_all_agenda'),
    path('delete_all_climed/', delete_all_climed, name='delete_all_climed'),
]
