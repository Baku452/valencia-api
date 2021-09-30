# Generated by Django 3.2 on 2021-09-29 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tripadvisorreviews',
            options={'verbose_name_plural': 'Trip Advisor Reviews'},
        ),
        migrations.AddField(
            model_name='tripadvisorreviews',
            name='title',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='tripadvisorreviews',
            name='url',
            field=models.CharField(default='', max_length=255),
        ),
    ]