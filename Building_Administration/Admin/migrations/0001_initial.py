# Generated by Django 3.2 on 2021-04-28 13:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Homeowners', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='Nombre de Edificio')),
            ],
            options={
                'verbose_name': 'Edificio',
                'verbose_name_plural': 'Edificios',
            },
        ),
        migrations.CreateModel(
            name='Apartament',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=200, unique=True, verbose_name='Codigo')),
                ('ph', models.CharField(max_length=50, verbose_name='PH')),
                ('address', models.CharField(max_length=200, verbose_name='Numeracion')),
                ('average', models.FloatField(verbose_name='Porcentaje Correspondiente')),
                ('balance_due', models.FloatField(verbose_name='Deuda')),
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.building', verbose_name='Edificio')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Homeowners.homeowner', verbose_name='Dueño')),
            ],
            options={
                'verbose_name': 'Departamento',
                'verbose_name_plural': 'Departamentos',
            },
        ),
    ]
