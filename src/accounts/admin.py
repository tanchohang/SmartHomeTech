from django.contrib import admin
from .models import UserDetail, AddressInfo, ContactDetail

# Register your models here.
admin.site.register(UserDetail)
admin.site.register(AddressInfo)
admin.site.register(ContactDetail)
