# Generated by Django 3.2 on 2021-06-28 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('specialists', '0010_auto_20210420_1645'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactusb2c',
            old_name='country_residence',
            new_name='country',
        ),
        migrations.RemoveField(
            model_name='contactusb2c',
            name='accommodation',
        ),
        migrations.RemoveField(
            model_name='contactusb2c',
            name='adults',
        ),
        migrations.RemoveField(
            model_name='contactusb2c',
            name='children',
        ),
        migrations.RemoveField(
            model_name='contactusb2c',
            name='departureDate',
        ),
        migrations.RemoveField(
            model_name='contactusb2c',
            name='destination_interest',
        ),
        migrations.RemoveField(
            model_name='contactusb2c',
            name='internationalFlight',
        ),
        migrations.RemoveField(
            model_name='contactusb2c',
            name='lengthStay',
        ),
        migrations.AddField(
            model_name='contactusb2c',
            name='city',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='contactusb2c',
            name='state',
            field=models.CharField(default='', max_length=255),
        ),
    ]