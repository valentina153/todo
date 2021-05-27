from django.urls import path
from . import views

app_name = 'autentikacija'

urlpatterns = [
    path('', views.registracija, name = 'registracija'),
    path('prijava/', views.prijava, name = 'prijava'),
    path('odjava/', views.odjava, name = 'odjava'),
]
