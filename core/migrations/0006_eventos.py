# Generated by Django 5.0.4 on 2024-04-10 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_usuario_edad_alter_usuario_fecha_nacimiento_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Eventos',
            fields=[
                ('idEvento', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('nombre_ev', models.CharField(max_length=50)),
                ('fecha', models.DateField()),
                ('lugar', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=100)),
            ],
        ),
    ]
