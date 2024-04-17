# Generated by Django 5.0.1 on 2024-04-17 12:13

import clothesDjango.catalogue.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0007_cloth_photo_6'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cloth',
            name='photo',
            field=models.ImageField(blank=True, max_length=300, null=True, upload_to='clothes_images', validators=[clothesDjango.catalogue.validators.image_size_validator]),
        ),
        migrations.AlterField(
            model_name='cloth',
            name='photo_2',
            field=models.ImageField(blank=True, max_length=300, null=True, upload_to='clothes_images', validators=[clothesDjango.catalogue.validators.image_size_validator]),
        ),
        migrations.AlterField(
            model_name='cloth',
            name='photo_3',
            field=models.ImageField(blank=True, max_length=300, null=True, upload_to='clothes_images', validators=[clothesDjango.catalogue.validators.image_size_validator]),
        ),
        migrations.AlterField(
            model_name='cloth',
            name='photo_4',
            field=models.ImageField(blank=True, max_length=300, null=True, upload_to='clothes_images', validators=[clothesDjango.catalogue.validators.image_size_validator]),
        ),
        migrations.AlterField(
            model_name='cloth',
            name='photo_5',
            field=models.ImageField(blank=True, max_length=300, null=True, upload_to='clothes_images', validators=[clothesDjango.catalogue.validators.image_size_validator]),
        ),
        migrations.AlterField(
            model_name='cloth',
            name='photo_6',
            field=models.ImageField(blank=True, max_length=300, null=True, upload_to='clothes_images', validators=[clothesDjango.catalogue.validators.image_size_validator]),
        ),
    ]
