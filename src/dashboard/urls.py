from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.enduser.dashboard, name='dashboard'),
    path('quotes/', views.enduser.quotes, name='quotes'),
    path('profile/<str:username>', views.enduser.profile, name='profile'),
    path('messages/', views.enduser.messages, name='message'),
    path('messages/<id>/', views.enduser.message_detail, name='message-detail'),
    path('messages/<id>/delete', views.enduser.message_delete),
    path('appointment/', views.enduser.appointment, name='appointment'),


    # Host URL

    # path('host/', views.host.dashboard, name='host'),
    path('users/', views.host.users, name='users'),
    # path('host/quotes/', views.host.quotes),
    # path('host/profile/', views.host.profile),
    # path('host/messages/', views.host.messages),
    # path('host/messages/<id>/',
    #      views.host.message_detail),



]
