# Generated by Django 5.0.4 on 2024-04-29 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_siteweb', '0005_hotel_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='nom',
            field=models.CharField(default="Nom d'hôtel inconnu", max_length=25),
        ),
    ]
