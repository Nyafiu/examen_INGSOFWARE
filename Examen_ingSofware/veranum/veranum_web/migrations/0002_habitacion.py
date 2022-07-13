# Generated by Django 4.0.5 on 2022-07-12 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veranum_web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Habitacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_habitacion', models.CharField(max_length=30)),
                ('hotel', models.IntegerField(choices=[(1, 'Hotel Santiago'), (2, 'Hotel Valparaiso')])),
                ('habitaciones', models.CharField(max_length=30)),
                ('camas', models.CharField(max_length=30)),
                ('banos', models.CharField(max_length=30)),
                ('foto', models.ImageField(upload_to='media')),
                ('wifi', models.BooleanField(default=False)),
                ('fumar', models.BooleanField(default=False)),
                ('tv', models.BooleanField(default=False)),
                ('jacuzzi', models.BooleanField(default=False)),
                ('descripcion', models.CharField(max_length=150)),
                ('precio', models.CharField(max_length=30)),
                ('oferta', models.BooleanField(default=False)),
            ],
        ),
    ]