# Generated by Django 3.1.4 on 2021-02-25 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ourPurpose', '0002_ourpurpose_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ourpurpose',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='ourpurpose',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
    ]