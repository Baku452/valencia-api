# Generated by Django 3.2.9 on 2022-02-28 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destinations', '0017_remove_destination_tailor_made'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='descriptionSEO',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='destination',
            name='titleSEO',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]