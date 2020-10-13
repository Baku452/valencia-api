# Generated by Django 3.1.1 on 2020-10-13 18:03

from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('packages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Itinerary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtitle', models.CharField(default='', max_length=255)),
                ('content', tinymce.models.HTMLField()),
                ('active', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('package', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='itineraries', to='packages.package')),
            ],
            options={
                'db_table': 'itinerary',
            },
        ),
        migrations.CreateModel(
            name='ItineraryImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', imagekit.models.fields.ProcessedImageField(upload_to='images/itinerary/')),
                ('alt', models.CharField(default='', max_length=255)),
                ('itinerary', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='itineraries.itinerary')),
            ],
            options={
                'db_table': 'itinerary_image',
            },
        ),
    ]
