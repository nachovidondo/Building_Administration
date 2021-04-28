from django.db import models
from Homeowners.models import Homeowner



class Building(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 50 ,verbose_name="Nombre de Edificio")
    class Meta:
        verbose_name ="Edificio"
        verbose_name_plural = "Edificios"
        
    def __str__(self):
        return self.name


class Apartament(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=200,unique=True, verbose_name="Codigo")
    ph = models.CharField(max_length=50, verbose_name="PH")
    address = models.CharField(max_length=200,verbose_name="Numeracion")
    average = models.FloatField(verbose_name="Porcentaje Correspondiente")
    balance_due = models.FloatField(verbose_name="Deuda")
    building = models.ForeignKey(Building, verbose_name="Edificio",
                                 on_delete=models.CASCADE)
    owner = models.ForeignKey(
        Homeowner, on_delete=models.CASCADE, verbose_name="Dueño")
    
    class Meta:
        verbose_name ="Departamento"
        verbose_name_plural ="Departamentos"
    
    def __str__(self):
        return self.ph
    