# Generated by Django 3.2 on 2021-05-06 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0034_package_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]