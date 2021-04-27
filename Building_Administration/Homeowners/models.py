from django.db import models
from Administration.models import Apartament



class Homeowner(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, verbose_name="Nombre")
    surname = models.CharField(max_length=200, verbose_name="Apellido")
    phone = models.CharField(max_length=200, verbose_name="Telefono")
    apartament = models.ForeignKey(
        Apartament, on_delete=models.CASCADE, verbose_name="Departamento")
    
    class Meta:
        verbose_name = "Dueño"
        verbose_name_plural = "Dueños"
    def __init__(self):
        return str(self.name + self.surname)
    