from django.core.validators import RegexValidator
from django.db import models


class Contacts(models.Model):
    name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=50, blank=True)
    phone_regex = RegexValidator(regex=r'^\+?7?\d{9,13}$',
                                 message="Phone number must be entered in the format: '+79999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=13, blank=True)

    def __str__(self):
        return self.name