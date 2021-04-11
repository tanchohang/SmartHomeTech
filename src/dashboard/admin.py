from django.contrib import admin
from .models import Message, Reply, Quote


admin.site.register(Message)
admin.site.register(Reply)
admin.site.register(Quote)
