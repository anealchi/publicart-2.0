# Generated by Django 4.2.15 on 2024-08-23 08:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('obra', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='estilo',
            old_name='descripción',
            new_name='descripcion',
        ),
    ]
