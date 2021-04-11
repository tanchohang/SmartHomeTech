from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.enduser.dashboard),
    path('user/quotes/', views.enduser.quotes),
    path('user/profile/', views.enduser.profile),
    path('user/messages/', views.enduser.messages),
    path('user/messages/<id>/', views.enduser.message_detail),
    path('user/messages/<id>/delete', views.enduser.message_delete),
    path('user/appointment/', views.enduser.appointment),




    # Contractor Url

    path('contractor/', views.contractor.dashboard),
    path('contractor/quotes/', views.contractor.quotes),
    path('contractor/profile/', views.contractor.profile),

    path('contractor/messages/', views.contractor.messages),
    path('contractor/messages/<id>/',
         views.contractor.message_detail),

    # Host URL

    path('host/', views.host.dashboard),
    path('host/users/', views.host.users),

    path('host/quotes/', views.host.quotes),
    path('host/profile/', views.host.profile),

    path('host/messages/', views.host.messages),
    path('host/messages/<id>/',
         views.host.message_detail),



]
