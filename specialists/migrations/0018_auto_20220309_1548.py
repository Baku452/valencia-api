# Generated by Django 3.2.9 on 2022-03-09 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('specialists', '0017_auto_20220301_1130'),
    ]

    operations = [
        migrations.AddField(
            model_name='tailorform',
            name='company',
            field=models.TextField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='tailorform',
            name='typeClient',
            field=models.TextField(default='', max_length=255),
        ),
    ]
