# Generated by Django 3.1.8 on 2021-04-14 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0028_package_highligths'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='video/packages/'),
        ),
    ]
