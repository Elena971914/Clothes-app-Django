# Generated by Django 5.0.1 on 2024-03-20 17:51

import clothesDjango.catalogue.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0006_alter_cloth_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='cloth',
            name='photo_1',
            field=models.ImageField(blank=True, null=True, upload_to='', validators=[clothesDjango.catalogue.validators.image_size_validator]),
        ),
        migrations.AddField(
            model_name='cloth',
            name='photo_2',
            field=models.ImageField(blank=True, null=True, upload_to='', validators=[clothesDjango.catalogue.validators.image_size_validator]),
        ),
        migrations.AddField(
            model_name='cloth',
            name='photo_3',
            field=models.ImageField(blank=True, null=True, upload_to='', validators=[clothesDjango.catalogue.validators.image_size_validator]),
        ),
        migrations.AddField(
            model_name='cloth',
            name='photo_4',
            field=models.ImageField(blank=True, null=True, upload_to='', validators=[clothesDjango.catalogue.validators.image_size_validator]),
        ),
        migrations.AddField(
            model_name='cloth',
            name='photo_5',
            field=models.ImageField(blank=True, null=True, upload_to='', validators=[clothesDjango.catalogue.validators.image_size_validator]),
        ),
    ]
