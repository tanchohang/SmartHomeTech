from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser, BaseUserManager


import uuid


# # Create your models here.
class ContactDetail(models.Model):
    phone_no = models.CharField(max_length=30)
    mobile_no = models.CharField(max_length=30)


class AddressInfo(models.Model):

    address_1 = models.CharField(max_length=100)
    address_2 = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    postcode = models.CharField(max_length=30)


class UserDetail(models.Model):
    company_name = models.CharField(max_length=100, blank=True)
    department = models.CharField(max_length=100, blank=True)
    position = models.CharField(max_length=100, blank=True)

    designation = models.CharField(max_length=50, blank=True)

    address = models.OneToOneField(AddressInfo, on_delete=models.CASCADE)
    contact = models.OneToOneField(ContactDetail, on_delete=models.CASCADE)

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)

# class Service(models.Model):
#     title = models.CharField(max_length=99)
#     description = models.CharField(max_length=255)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)


# class MyUserManager(BaseUserManager):
#     def create_user(self, email, username, password=None):
#         if not email:
#             raise ValueError('Users must have an email address')
#         if not username:
#             raise ValueError('Users must have an username')
#         user = self.model(
#             email=self.normalize_email(email),
#             username=username
#         )
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, username, password=None):
#         user = self.create_user(
#             email=self.normalize_email(email),
#             username=username,
#             password=password,
#         )
#         user.is_admin = True
#         user.is_staff = True
#         user._is_superuser = True
#         user.save(using=self._db)
#         return user


# class MyUser(AbstractUser):
#     email = models.EmailField(verbose_name="email", max_length=60, unique=True)
#     username = models.EmailField(max_length=30, unique=True)
#     date_joined = models.DateTimeField(
#         verbose_name="date joined", auto_now_add=True)
#     last_login = models.DateTimeField(
#         verbose_name="last login", auto_now=True)
#     is_admin = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)

#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username']
#     objects = MyUserManager()

#     def __str__(self):
#         return self.username

#     def has_perm(self, perm, obj=None):
#         return self.is_admin

#     def has_module_perms(self, app_label):
#         return True
