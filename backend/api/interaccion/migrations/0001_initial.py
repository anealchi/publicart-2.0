# Generated by Django 4.2.15 on 2024-08-23 11:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('creacion', models.DateTimeField(auto_now_add=True)),
                ('participantes', models.ManyToManyField(related_name='chats', to='authentication.perfil')),
            ],
            options={
                'verbose_name_plural': 'Chats',
            },
        ),
        migrations.CreateModel(
            name='Mensaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(max_length=500)),
                ('fecha_mensaje', models.DateTimeField(auto_now_add=True)),
                ('leido', models.BooleanField(default=False)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='authentication.perfil')),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='interaccion.chat')),
            ],
            options={
                'verbose_name_plural': 'Mensajes',
            },
        ),
        migrations.CreateModel(
            name='Seguimiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_seguimiento', models.DateTimeField(auto_now_add=True)),
                ('seguido', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='seguidos', to='authentication.perfil')),
                ('seguidor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='seguidores', to='authentication.perfil')),
            ],
            options={
                'verbose_name_plural': 'Seguimientos',
                'unique_together': {('seguidor', 'seguido')},
            },
        ),
    ]
