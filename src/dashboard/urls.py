from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('quotes/', views.quotes),
    path('profile/', views.profile),

    path('messages/', views.messages),
    path('messages/<id>/', views.message_detail),
    path('messages/<id>/delete', views.message_delete),
    path('appointment/', views.appointment),




    # Contractor Url

    path('contractor/', views.contractor_home),
    path('contractor/quotes/', views.contractor_quotes),
    path('contractor/profile/', views.contractor_profile),

    path('contractor/messages/', views.contractor_messages),
    path('contractor/messages/message-detail/',
         views.contractor_message_detail),

    # Host URL

    path('host/', views.host_home),
    path('host/quotes/', views.host_quotes),
    path('host/profile/', views.host_profile),

    path('host/messages/', views.host_messages),
    path('host/messages/<id>/',
         views.host_message_detail),



]
