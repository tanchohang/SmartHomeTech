from django.db import models
from accounts.models import UserDetail, AddressInfo


# Create your models here.

class Quote(models.Model):
    description = models.TextField()
    is_confirmed = models.BooleanField(default=False)
    quotation = models.CharField(max_length=30, blank=True)
    user = models.OneToOneField(UserDetail, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Message(models.Model):
    subject = models.CharField(max_length=150)
    body = models.TextField()
    summary = models.TextField(max_length=200)
    # files = models.FileField(upload_to='uploads/', null=True)
    # is_deleted = models.BooleanField(default=False)
    creator = models.ForeignKey(
        UserDetail, on_delete=models.CASCADE)
    quote = models.OneToOneField(
        Quote, on_delete=models.CASCADE, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)


class MessageFiles(models.Model):
    files = models.FileField(upload_to="uploads/", null=True, blank=True)
    message = models.ForeignKey(Message, on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)


class Reply(models.Model):
    body = models.TextField()
    is_read = models.BooleanField(default=False)
    files = models.FileField(upload_to='uploads/')
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    author = models.ForeignKey(UserDetail, on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)


class Appointment(models.Model):
    date = models.DateField()
    time = models.TimeField()
    preference = models.CharField(max_length=10)
    phone = models.CharField(max_length=50)
    user = models.ForeignKey(UserDetail, on_delete=models.CASCADE)
    quote = models.ForeignKey(Quote, on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)


class Project(models.Model):
    name = models.CharField(max_length=100)
    cost = models.CharField(max_length=50, blank=True)
    description = models.TextField()
    address = models.ForeignKey(AddressInfo, on_delete=models.CASCADE)
    owner = models.ForeignKey(
        UserDetail, on_delete=models.CASCADE, related_name='project_owner')
    contractor = models.ForeignKey(
        UserDetail, on_delete=models.CASCADE, related_name='project_contractor')
    quote = models.ForeignKey(Quote, on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)
