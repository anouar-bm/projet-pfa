# Generated by Django 5.0.4 on 2024-04-29 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_siteweb', '0004_remove_hotel_num_tel_hotel_num_telephone_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='description',
            field=models.TextField(default='Aucune description fournie'),
        ),
    ]
