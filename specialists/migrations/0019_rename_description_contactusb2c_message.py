# Generated by Django 3.2.9 on 2022-03-17 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('specialists', '0018_auto_20220309_1548'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactusb2c',
            old_name='description',
            new_name='message',
        ),
    ]
