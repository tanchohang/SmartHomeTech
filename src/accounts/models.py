from django.db import models
from django.contrib.auth.models import User

import uuid


# # Create your models here.

class AddressInfo(models.Model):
    phone_no = models.CharField(max_length=30)
    mobile_no = models.CharField(max_length=30)
    address_1 = models.CharField(max_length=100)
    address_2 = models.CharField(max_length=100)
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    postcode = models.CharField(max_length=30)


class UserDetail(models.Model):
    company_name = models.CharField(max_length=100, blank=True)
    department = models.CharField(max_length=100, blank=True)
    position = models.CharField(max_length=100, blank=True)

    address = models.OneToOneField(AddressInfo, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)


# class Service(models.Model):
#     title = models.CharField(max_length=99)
#     description = models.CharField(max_length=255)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)


# class Project(models.Model):
#     cost = models.IntegerField()
#     description = models.TextField()
#     street = models.CharField(30)
#     city = models.CharField(30)
#     postcode = models.CharField(10)
#     # userId = models.ForeignKey(User, on_delete=models.CASCADE)
#     serviceId = models.ManyToManyField(Service, on_delete=models.CASCADE)
#     contractorId = models.ForeignKey(Contractor, on_delete=models.CASCADE)
