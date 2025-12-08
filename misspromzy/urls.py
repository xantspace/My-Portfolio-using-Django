from django.urls import path
from misspromzy import views

urlpatterns = [
    path('', views.home, name='Index'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
]