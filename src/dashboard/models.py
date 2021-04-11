from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Quote(models.Model):
    description = models.TextField()
    is_confirmed = models.BooleanField(default=False)
    quotation = models.CharField(max_length=30, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Message(models.Model):
    subject = models.CharField(max_length=150)
    body = models.TextField()
    summary = models.TextField(max_length=200)
    files = models.FileField(upload_to='uploads/')
    # is_deleted = models.BooleanField(default=False)
    creator = models.ForeignKey(
        User, on_delete=models.CASCADE)
    quote = models.OneToOneField(
        Quote, on_delete=models.CASCADE, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)


class Reply(models.Model):
    body = models.TextField()
    is_read = models.BooleanField(default=False)
    files = models.FileField(upload_to='uploads/')
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


class Appointment(models.Model):
    date = models.DateField()
    time = models.TimeField()
    preference = models.CharField(max_length=10)
    phone = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quote = models.ForeignKey(Quote, on_delete=models.CASCADE)
