# Generated by Django 5.0.1 on 2024-04-06 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('likes_cart', '0004_cart_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
