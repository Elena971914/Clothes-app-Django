# Generated by Django 5.0.1 on 2024-04-20 13:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0011_cloth_creation_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cloth',
            options={'ordering': ['-creation_date'], 'verbose_name_plural': 'Clothes'},
        ),
    ]
