# Generated by Django 3.2.9 on 2022-02-28 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('specialists', '0015_auto_20211102_1033'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactus',
            old_name='message',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='contactusb2c',
            old_name='message',
            new_name='description',
        ),
    ]
