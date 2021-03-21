from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('login/', views.login),
    path('register/', views.register),
    path('services/', views.services),
    path('portfolio/', views.portfolio),
    path('about/', views.about),
    path('contact/', views.contact),
    path('estimator/', views.estimator),
]
