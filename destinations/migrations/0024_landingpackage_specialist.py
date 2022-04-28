# Generated by Django 3.2.9 on 2022-04-28 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('specialists', '0023_specialist_calendly'),
        ('destinations', '0023_landingpackage_banner'),
    ]

    operations = [
        migrations.AddField(
            model_name='landingpackage',
            name='specialist',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='specialist_landing', to='specialists.specialist'),
        ),
    ]