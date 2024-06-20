# Generated by Django 5.0.6 on 2024-06-18 15:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Capteur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idcapteur', models.IntegerField()),
                ('nom', models.CharField(max_length=100)),
                ('piece', models.CharField(max_length=100)),
                ('emplacement', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Donnees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jour', models.DateField()),
                ('heure', models.TimeField()),
                ('temp', models.DecimalField(decimal_places=2, max_digits=5)),
                ('idcapteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.capteur')),
            ],
        ),
    ]