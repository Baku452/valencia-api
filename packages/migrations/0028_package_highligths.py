# Generated by Django 3.1.8 on 2021-04-14 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0027_auto_20210414_0019'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='highligths',
            field=models.TextField(blank=True, default='', max_length=255),
        ),
    ]