from django.contrib import admin
from .models import EndUser, Contractor, AddressInfo

# Register your models here.
admin.site.register(EndUser)
admin.site.register(Contractor)
admin.site.register(AddressInfo)
