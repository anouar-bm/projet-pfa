# Generated by Django 5.0.4 on 2024-04-30 12:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_siteweb', '0010_remove_ville_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='rating',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
