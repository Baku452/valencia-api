# Generated by Django 3.2 on 2021-06-22 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0036_auto_20210614_0855'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='package',
            name='video',
        ),
        migrations.AlterField(
            model_name='package',
            name='titleSEO',
            field=models.TextField(blank=True, default='', max_length=255),
        ),
    ]
