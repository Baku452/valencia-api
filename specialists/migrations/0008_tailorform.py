# Generated by Django 3.1.8 on 2021-04-19 20:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('specialists', '0007_remove_contactusb2c_budget'),
    ]

    operations = [
        migrations.CreateModel(
            name='TailorForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=255)),
                ('last_name', models.CharField(default='', max_length=255)),
                ('email', models.EmailField(default='', max_length=255)),
                ('number', models.CharField(default='', max_length=255)),
                ('destination_interest', models.CharField(default='', max_length=255)),
                ('accommodation', models.CharField(default='', max_length=255)),
                ('departureDate', models.DateField(default=datetime.date.today)),
                ('lengthStay', models.CharField(default='', max_length=255)),
                ('adults', models.IntegerField(default=0)),
                ('children', models.IntegerField(default=0)),
                ('internationalFlight', models.CharField(default='', max_length=255)),
                ('budget', models.CharField(default='', max_length=255)),
                ('trip_type', models.CharField(default='', max_length=255)),
                ('hear_about', models.CharField(default='', max_length=255)),
                ('message', models.TextField(default='', max_length=999)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'tailorForm',
            },
        ),
    ]
