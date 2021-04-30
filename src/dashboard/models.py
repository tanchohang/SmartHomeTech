from django.db import models
from accounts.models import UserDetail, AddressInfo
import datetime


# Create your models here.

class Quote(models.Model):
    description = models.TextField()
    is_confirmed = models.BooleanField(default=False)
    quotation = models.CharField(max_length=30, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Message(models.Model):
    subject = models.CharField(max_length=150, blank=True)
    body = models.TextField()
    creator = models.ForeignKey(
        UserDetail, on_delete=models.CASCADE)
    project = models.ForeignKey(
        "dashboard.Project", on_delete=models.CASCADE, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)


class ProjectFiles(models.Model):
    file = models.FileField(upload_to="uploads/", null=True, blank=True)
    project = models.ForeignKey("dashboard.Project", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)


class Appointment(models.Model):
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    preference = models.CharField(max_length=10)
    phone = models.CharField(max_length=50)
    quote = models.OneToOneField(Quote, on_delete=models.CASCADE)
    is_confirmed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)


class Project(models.Model):
    name = models.CharField(max_length=100)
    cost = models.CharField(max_length=50, blank=True)
    description = models.TextField()
    address = models.ForeignKey(AddressInfo, on_delete=models.CASCADE)
    owner = models.ForeignKey(
        UserDetail, on_delete=models.CASCADE, related_name='project_owner')

    quote = models.OneToOneField(
        Quote,  on_delete=models.CASCADE, blank=True, null=True)
    contractor_confirmed = models.BooleanField(default=False)
    contractor = models.ForeignKey(
        UserDetail, blank=True, null=True, on_delete=models.SET_NULL)

    created = models.DateTimeField(auto_now_add=True)
