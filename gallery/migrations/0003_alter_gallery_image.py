# Generated by Django 5.0.7 on 2025-03-23 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_remove_gallery_image_urls_gallery_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='image',
            field=models.URLField(),
        ),
    ]
