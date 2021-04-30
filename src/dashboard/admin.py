from django.contrib import admin
from .models import Message, Quote, Project, Appointment


admin.site.register(Message)
admin.site.register(Quote)
admin.site.register(Project)
admin.site.register(Appointment)
