# Generated by Django 3.1.2 on 2020-10-23 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destinations', '0003_auto_20201022_2002'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='tailor_made',
            field=models.BooleanField(default=False),
        ),
    ]
