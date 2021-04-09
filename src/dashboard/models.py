from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Message(models.Model):
    subject = models.CharField(max_length=150)
    body = models.TextField()
    summary = models.TextField(max_length=200)
    # files = models.FileField(upload_to='uploads/')
    # is_deleted = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True)

    creator = models.ForeignKey(
        User, on_delete=models.CASCADE)


class Reply(models.Model):
    body = models.TextField()
    # files = models.FileField(upload_to='uploads/')
    is_read = models.BooleanField(default=False)
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    author = models.ForeignKey(
        User, on_delete=models.CASCADE)


class Appointment(models.Model):
    date = models.DateField()
    time = models.TimeField()
    preference = models.CharField(max_length=10)
    phone = models.CharField(max_length=50)

    user = models.ForeignKey(
        User, on_delete=models.CASCADE)
