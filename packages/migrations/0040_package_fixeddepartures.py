# Generated by Django 3.2 on 2021-09-07 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0039_auto_20210727_1045'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='fixedDepartures',
            field=models.TextField(blank=True, default='', max_length=255),
        ),
    ]
