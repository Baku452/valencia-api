# Generated by Django 3.2.8 on 2021-11-16 16:19

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ourteam', '0009_alter_collaborator_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collaborator',
            name='slug',
            field=autoslug.fields.AutoSlugField(always_update=True, editable=False, populate_from='full_name', unique_with=['name']),
        ),
    ]
