# Generated by Django 4.0.5 on 2022-07-12 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veranum_web', '0003_reserva'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trabajador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('genero', models.IntegerField(choices=[(1, 'Hombre'), (2, 'Mujeres')])),
                ('fecha_nacimiento', models.DateField(default=False)),
                ('edad', models.CharField(max_length=30)),
                ('correo', models.CharField(max_length=30)),
                ('cargo', models.CharField(max_length=30)),
                ('vigente', models.BooleanField()),
            ],
        ),
    ]
