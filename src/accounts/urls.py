from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('login/', views.login),
    path('products/', views.products),
    path('portfolio/', views.portfolio),
    path('about/', views.about),
    path('contact/', views.contact),
    path('estimator/', views.estimator),
    
]
