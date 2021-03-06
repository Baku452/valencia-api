# Generated by Django 3.1.4 on 2021-02-01 03:32

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
      
        ('itineraries', '0006_auto_20210122_1540'),
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
                ('package', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='optionals', to='packages.package')),
            ],
            options={
                'db_table': 'optional_renting',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=255)),
                ('content', tinymce.models.HTMLField()),
                ('order', models.PositiveIntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('package', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='faqs', to='packages.package')),
            ],
            options={
                'db_table': 'faq',
                'ordering': ['order'],
            },
        ),
    ]
