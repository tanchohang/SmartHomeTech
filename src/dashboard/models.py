from django.db import models

# Create your models here.


class Message(models.Model):

    user = models.ForeignKey("AddressInfo", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
