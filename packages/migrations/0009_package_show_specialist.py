# Generated by Django 3.1.2 on 2020-10-26 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0008_auto_20201023_2327'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='show_specialist',
            field=models.BooleanField(default=False),
        ),
    ]
