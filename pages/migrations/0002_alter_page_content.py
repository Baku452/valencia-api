# Generated by Django 3.2 on 2021-10-06 21:03

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
