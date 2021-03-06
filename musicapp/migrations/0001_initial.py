# Generated by Django 3.2.9 on 2021-11-15 01:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_album', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('duracion', models.TextField()),
                ('artista', models.TextField()),
                ('imagen_album', models.TextField()),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='music', to='musicapp.album')),
            ],
        ),
    ]
