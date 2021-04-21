from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.user.dashboard, name='dashboard'),
    path('quotes/', views.user.quotes, name='quotes'),
    path('profile/<str:username>', views.user.profile, name='profile'),
    path('messages/', views.user.messages, name='message'),
    path('messages/<id>/', views.user.message_detail, name='message-detail'),
    path('messages/<id>/delete', views.user.message_delete),
    path('appointment/', views.user.appointment, name='appointment'),


    # Host URL

    # path('host/', views.host.dashboard, name='host'),
    path('users/', views.host.users, name='users'),
    # path('host/quotes/', views.host.quotes),
    # path('host/profile/', views.host.profile),
    # path('host/messages/', views.host.messages),
    # path('host/messages/<id>/',
    #      views.host.message_detail),



]
