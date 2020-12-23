# Generated by Django 3.1.2 on 2020-10-23 04:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0006_auto_20201022_2028'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='packagetype',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='packagetype',
            name='svg',
            field=models.FileField(default='', upload_to='images/package_type/', validators=[django.core.validators.FileExtensionValidator(['svg'])]),
        ),
    ]