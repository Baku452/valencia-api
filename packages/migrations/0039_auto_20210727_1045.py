# Generated by Django 3.2 on 2021-07-27 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0038_alter_package_optional_forrenting'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='incatrail',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='package',
            name='activity',
            field=models.IntegerField(choices=[(1, 'Very High'), (2, 'High'), (3, 'Moderate'), (4, 'Low')], default=1),
        ),
    ]