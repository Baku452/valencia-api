# Generated by Django 3.2.9 on 2022-04-27 22:31

from django.db import migrations
import imagekit.models.fields
import packages.models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0050_auto_20220315_1416'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(blank=True, upload_to=packages.models.path_and_rename),
        ),
    ]