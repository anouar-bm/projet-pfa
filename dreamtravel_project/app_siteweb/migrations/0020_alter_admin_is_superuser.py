# Generated by Django 5.0.4 on 2024-05-01 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_siteweb', '0019_remove_client_nom_remove_client_prenom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]
