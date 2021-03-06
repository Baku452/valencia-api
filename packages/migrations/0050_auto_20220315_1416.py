# Generated by Django 3.2.9 on 2022-03-15 19:16

from django.db import migrations, models
import imagekit.models.fields
import packages.models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0049_packagetype_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='packagetype',
            name='descriptionSEO',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='packagetype',
            name='keywordsSEO',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='packagetype',
            name='thumbnail',
            field=imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to=packages.models.path_and_rename_packageType),
        ),
        migrations.AddField(
            model_name='packagetype',
            name='titleSEO',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='packagetype',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to=packages.models.path_and_rename_packageType),
        ),
    ]
