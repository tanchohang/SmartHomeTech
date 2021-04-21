from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),


    path('services/', views.services),

    path('portfolio/', views.portfolio),
    path('about/', views.about),
    path('contact/', views.contact),

    path('register/', views.registerPage, name='register'),
    path('contractor/register/', views.contractorRegisterPage),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser),


]
