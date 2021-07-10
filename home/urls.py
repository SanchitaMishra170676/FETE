from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.home, name='home'),
    path('gallery/', views.gallery, name='gallery'),
    path('contact-us/', views.contact, name='contact'),
    path('team/',views.team,name='team'),
    path('donation/', views.donation, name='donation'),
]