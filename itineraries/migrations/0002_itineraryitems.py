# Generated by Django 3.1.1 on 2020-10-15 19:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('itineraries', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItineraryItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('types', models.CharField(choices=[('Meals Included', 'Meals Included'), ('Accommodations', 'Accommodations')], default='', max_length=100)),
                ('text', models.CharField(default='', max_length=255)),
                ('itinerary', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='itineraries.itinerary')),
            ],
            options={
                'db_table': 'itinerary_items',
            },
        ),
    ]
