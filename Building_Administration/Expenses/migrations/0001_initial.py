# Generated by Django 3.2 on 2021-04-29 13:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Admin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expensas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('payment', models.BooleanField(default=False, verbose_name='Pago')),
                ('expensas_puras', models.FloatField(blank=True, null=True, verbose_name='Expensas Puras')),
                ('total_ingresos', models.FloatField(blank=True, null=True, verbose_name='Total ingresos')),
                ('deuda_totales', models.FloatField(blank=True, null=True, verbose_name='Total Adeudado')),
                ('intereses_mora', models.FloatField(blank=True, null=True, verbose_name='Intereses por Mora')),
                ('materiales_limpieza', models.FloatField(blank=True, null=True, verbose_name='materiales de limpieza')),
                ('servicios_luz', models.FloatField(blank=True, null=True, verbose_name='servicios electricidad')),
                ('gastos_electricidad', models.FloatField(blank=True, null=True, verbose_name='materiales y mano obra electricidad')),
                ('gastos_pintura', models.FloatField(blank=True, null=True, verbose_name='materiales y mano obra pintura')),
                ('gastos_cerrajeria', models.FloatField(blank=True, null=True, verbose_name=' materiales y mano de obra cerrajeria')),
                ('gastos_portero_electrico', models.FloatField(blank=True, null=True, verbose_name='service portero electrico')),
                ('gastos_bomba_agua', models.FloatField(blank=True, null=True, verbose_name='service bombas de agua')),
                ('gastos_matafuegos', models.FloatField(blank=True, null=True, verbose_name=' recarga matafuegos')),
                ('gastos_accesorios', models.FloatField(blank=True, null=True, verbose_name=' gastos accesorios')),
                ('vacaciones_encargado', models.FloatField(blank=True, null=True, verbose_name=' vacaciones encargado')),
                ('reemplazo_encargado', models.FloatField(blank=True, null=True, verbose_name=' reemplazo encargado')),
                ('sueldo_administrador', models.FloatField(blank=True, null=True, verbose_name='Sueldo Administrador')),
                ('ascensores', models.FloatField(blank=True, null=True, verbose_name='Gasto Ascensores')),
                ('aportes_encargado_limpieza', models.FloatField(blank=True, null=True, verbose_name='Aportes Encargado Limpieza')),
                ('sueldo_encargado_limpieza', models.FloatField(blank=True, null=True, verbose_name='Sueldo Encargado Limpieza')),
                ('seguro_edificio', models.FloatField(blank=True, null=True, verbose_name='Seguro Edificio')),
                ('sueldo_anual_complementario', models.FloatField(blank=True, null=True, verbose_name='Sueldo Anual Complementario')),
                ('total_gastos', models.FloatField(blank=True, null=True, verbose_name='Total de Gastos (Egreso)')),
                ('create_date', models.DateTimeField(auto_now=True, verbose_name='Fecha Creacion')),
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.building', verbose_name='Edificio')),
            ],
            options={
                'verbose_name': 'Expensas',
                'verbose_name_plural': 'Expensas',
            },
        ),
    ]
