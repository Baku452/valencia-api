# Generated by Django 3.1.1 on 2020-10-18 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0003_remove_package_experience'),
        ('specialists', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsletter',
            name='package_type',
            field=models.ManyToManyField(to='packages.PackageType'),
        ),
    ]
