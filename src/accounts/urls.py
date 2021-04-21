from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('services/', views.services),

    path('portfolio/', views.portfolio),
    path('about/', views.about),
    path('contact/', views.contact),

    path('register/', views.registerPage),
    path('contractor/register/', views.contractorRegisterPage),
    path('login/', views.loginPage),
    path('logout/', views.logoutUser),

]
