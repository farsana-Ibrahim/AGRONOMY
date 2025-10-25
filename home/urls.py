from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name="index"),
    path('signupas',views.signupas,name="signupas"),
    path('loginas',views.loginas,name="loginas"),
    path('contact',views.contact,name="contact"),
    path('about',views.about,name="about"),
    path('details',views.details,name="details"),
]
