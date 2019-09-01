# Generated by Django 2.2.4 on 2019-08-29 12:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0002_auto_20190829_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='phone_number',
            field=models.CharField(blank=True, max_length=13, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+79999999999'. Up to 15 digits allowed.", regex='^\\+?7?\\d{9,13}$')]),
        ),
    ]