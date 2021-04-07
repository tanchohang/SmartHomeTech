from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('quotes/', views.quotes),
    path('profile/', views.profile),

    path('messages/', views.messages),
    path('messages/message-detail/', views.message_detail),


    # Contractor Url

    path('contractor/', views.contractor_home),
    path('contractor/quotes/', views.contractor_quotes),
    path('contractor/profile/', views.contractor_profile),

    path('contractor/messages/', views.contractor_messages),
    path('contractor/messages/message-detail/',
         views.contractor_message_detail),



]
