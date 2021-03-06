# Generated by Django 2.1.4 on 2019-01-07 13:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Pieza', '0005_piezaresultado'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fase',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nFase', models.IntegerField()),
                ('tiempoRequerido', models.FloatField()),
                ('maquinaNecesaria', models.IntegerField()),
                ('tiempoFaseEntrada', models.FloatField()),
                ('tiempoFaseSalida', models.FloatField()),
                ('ejecucion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pieza.Ejecucion')),
                ('nPieza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pieza.PiezaResultado')),
            ],
        ),
    ]
