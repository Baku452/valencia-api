# Generated by Django 3.2.8 on 2021-11-16 14:22

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Collaborator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('order', models.PositiveIntegerField(default=0)),
                ('slug', autoslug.fields.AutoSlugField(always_update=True, editable=False, populate_from=['name', 'last_name'], unique_with=['name', 'last_name'])),
                ('image', models.FileField(null=True, upload_to='images/ourteam/')),
            ],
            options={
                'db_table': 'collaborators',
                'ordering': ['order'],
            },
        ),
    ]
