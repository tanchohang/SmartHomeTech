from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('login/', views.loginPage),
    path('logout/', views.logoutUser),
    path('products/', views.products),
    path('portfolio/', views.portfolio),
    path('about/', views.about),
    path('contact/', views.contact),
    path('estimator/', views.estimator),
    path('register2/', views.registerPage),

]
