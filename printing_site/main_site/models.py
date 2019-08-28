from django.db import models

# Create your models here.


class Contacts(models.Model):
    name = models.TextField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.