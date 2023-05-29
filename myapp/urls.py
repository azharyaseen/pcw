from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('home', views.index, name="index"),
    path('search', views.search, name="search"),
    path('team', views.team, name="team"),
    path('contact', views.contact, name="contact"),
    path('about_us', views.about_us, name="about_us"),
    path('services', views.services, name="services"),
    path('register', views.register, name="register"),
    path('login', views.LoginPage, name="login"),
    path('subscribe', views.subscribe, name="subscribe"),
]
