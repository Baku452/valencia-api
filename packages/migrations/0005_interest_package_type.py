# Generated by Django 3.1.2 on 2020-10-22 20:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0004_auto_20201022_2002'),
    ]

    operations = [
        migrations.AddField(
            model_name='interest',
            name='package_type',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='interests', to='packages.packagetype'),
        ),
    ]
