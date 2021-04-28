from django.db import models
from Admin.models import Building



class Expensas(models.Model):
    id = models.AutoField(primary_key=True)
    payment = models.BooleanField(default=False, verbose_name="Pago")
    building = models.ForeignKey(
        Building, on_delete=models.CASCADE, verbose_name="Edificio")
    expensas_puras = models.FloatField(
        verbose_name="Expensas Puras",blank=True, null=True)
    total_ingresos = models.FloatField(
        verbose_name="Total ingresos",blank=True, null=True)
    deuda_totales = models.FloatField(
        verbose_name="Total Adeudado",blank=True, null=True)
    intereses_mora = models.FloatField(
        verbose_name="Intereses por Mora",blank=True, null=True)
    materiales_limpieza = models.FloatField(
        verbose_name="materiales de limpieza",blank=True, null=True)
    servicios_luz= models.FloatField(verbose_name="servicios electricidad",blank=True, null=True)
    gastos_electricidad=models.FloatField(
        verbose_name="materiales y mano obra electricidad",blank=True, null=True)
    gastos_pintura=models.FloatField(
        verbose_name="materiales y mano obra pintura",blank=True, null=True)
    gastos_cerrajeria=models.FloatField(
        verbose_name=" materiales y mano de obra cerrajeria",blank=True, null=True)
    gastos_portero_electrico=models.FloatField(
        verbose_name="service portero electrico",blank=True, null=True)
    gastos_bomba_agua=models.FloatField(
        verbose_name="service bombas de agua",blank=True, null=True)
    gastos_matafuegos=models.FloatField(
        verbose_name=" recarga matafuegos",blank=True, null=True)
    gastos_accesorios=models.FloatField(
        verbose_name=" gastos accesorios",blank=True, null=True)
    vacaciones_encargado =models.FloatField(
        verbose_name=" vacaciones encargado",blank=True, null=True)
    reemplazo_encargado=models.FloatField(
        verbose_name=" reemplazo encargado",blank=True, null=True)
    sueldo_administrador = models.FloatField(
        verbose_name="Sueldo Administrador",blank=True, null=True)
    ascensores = models.FloatField(
        verbose_name="Gasto Ascensores",blank=True, null=True)
    aportes_encargado_limpieza = models.FloatField(
        verbose_name="Aportes Encargado Limpieza",blank=True, null=True)
    sueldo_encargado_limpieza = models.FloatField(
        verbose_name="Sueldo Encargado Limpieza",blank=True, null=True)
    seguro_edificio = models.FloatField(
        verbose_name="Seguro Edificio",blank=True, null=True)
    sueldo_anual_complementario = models.FloatField(
        verbose_name="Sueldo Anual Complementario",blank=True, null=True)
    total_gastos = models.FloatField(
        verbose_name="Total de Gastos (Egreso)", blank=True, null=True)
    create_date = models.DateTimeField(
        auto_now=True, verbose_name="Fecha Creacion")
    
    class Meta:
        verbose_name = "Expensas"
        verbose_name_plural = "Expensas"
        
    def __str__(self):
        return self.id
    