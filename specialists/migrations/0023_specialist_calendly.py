# Generated by Django 3.2.9 on 2022-03-24 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('specialists', '0022_contactus_package'),
    ]

    operations = [
        migrations.AddField(
            model_name='specialist',
            name='calendly',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
    ]