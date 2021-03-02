# Generated by Django 3.1.7 on 2021-03-01 21:35

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields
import packages.models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0022_package_recommendations'),
    ]

    operations = [
        migrations.CreateModel(
            name='OptionalRenting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=255)),
                ('content', tinymce.models.HTMLField()),
                ('order', models.PositiveIntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'optional_Renting',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='OptionalRentingImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alt', models.CharField(default='', max_length=255)),
                ('slug', autoslug.fields.AutoSlugField(always_update=True, editable=False, populate_from='alt', unique_with=['alt'])),
                ('image', imagekit.models.fields.ProcessedImageField(upload_to=packages.models.path_and_rename)),
                ('optional_renting', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='packages.optionalrenting')),
            ],
            options={
                'db_table': 'optionalRenting_Image',
            },
        ),
        migrations.AddField(
            model_name='package',
            name='optional_forRenting',
            field=models.ManyToManyField(to='packages.OptionalRenting'),
        ),
    ]
