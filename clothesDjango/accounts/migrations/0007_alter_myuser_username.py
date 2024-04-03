# Generated by Django 5.0.1 on 2024-04-03 16:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_myuser_city_myuser_postal_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='username',
            field=models.CharField(max_length=150, unique=True, validators=[django.core.validators.MinLengthValidator(4, message='Username must be at least 4 characters long.'), django.core.validators.RegexValidator('^\\S+$', message='Username cannot contain spaces.')]),
        ),
    ]
