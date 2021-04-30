from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.user.dashboard, name='dashboard'),
    path('quotes/', views.user.quotes, name='quotes'),
    path('profile/<username>', views.user.profile, name='profile'),
    path('messages/', views.user.messages, name='message'),
    path('messages/<id>/', views.user.message_detail, name='message-detail'),
    path('messages/<id>/delete', views.user.message_delete),
    path('appointment/<appointment>', views.user.appointment, name='appointment'),
    path('projects/', views.user.projects, name='projects'),




    # Contractor url
    path('user_requests/', views.user.user_requests, name='user-requests'),
    path('user_requests/<int:project>',
         views.user.user_requests_confirmation, name='request-confirm'),



    # Host URL


    path('users/', views.host.users, name='users'),
    path('user/<project_id>/contractor/<contractor_id>', views.host.assign_contractor,
         name='assign-contractor'),

    path('projects/<project>/appointment/',
         views.host.appointment, name='host-appointment'),

    path('quotes/<quote>', views.user.quotation, name='quotation'),







]
