# Generated by Django 3.2.8 on 2021-11-17 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ourteam', '0011_collaborator_job'),
    ]

    operations = [
        migrations.AddField(
            model_name='collaborator',
            name='hobbies',
            field=models.TextField(default=''),
        ),
    ]
