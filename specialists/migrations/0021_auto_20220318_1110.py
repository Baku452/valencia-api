# Generated by Django 3.2.9 on 2022-03-18 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('specialists', '0020_auto_20220318_0909'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactus',
            old_name='country_residence',
            new_name='country',
        ),
        migrations.RenameField(
            model_name='contactus',
            old_name='description',
            new_name='message',
        ),
    ]
