# Generated by Django 3.2.8 on 2021-11-18 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destinations', '0012_banner_extracta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='extraCTA',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
