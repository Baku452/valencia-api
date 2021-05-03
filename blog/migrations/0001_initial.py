# Generated by Django 3.1.8 on 2021-04-12 23:32

import autoslug.fields
import blog.models
import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('destinations', '0010_auto_20210209_1529'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('active', models.BooleanField(default=False)),
                ('order', models.PositiveIntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'blog_type',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=255)),
                ('keywords', models.TextField(default='')),
                ('titleSEO', models.TextField(default='', max_length=255)),
                ('slug', autoslug.fields.AutoSlugField(always_update=True, editable=False, populate_from='title', unique_with=['title'])),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('thumbnail', imagekit.models.fields.ProcessedImageField(blank=True, upload_to=blog.models.path_and_rename)),
                ('banner', imagekit.models.fields.ProcessedImageField(blank=True, upload_to=blog.models.path_and_rename)),
                ('published', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('blog_type', models.ManyToManyField(to='blog.BlogType')),
                ('destination', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='destinations.destination')),
            ],
            options={
                'db_table': 'blog_posts',
            },
        ),
    ]
