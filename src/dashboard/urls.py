from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('quotes/', views.quotes),
    path('profile/', views.profile),

    path('messages/', views.messages),


]