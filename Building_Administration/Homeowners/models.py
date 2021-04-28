from django.db import models
from Admin.models import Apartament



class Homeowner(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, verbose_name="Nombre")
    surname = models.CharField(max_length=200, verbose_name="Apellido")
    phone = models.CharField(max_length=200, verbose_name="Telefono")
    email = models.EmailField(default="No tiene")
    apartament = models.ForeignKey(
        Apartament, on_delete=models.CASCADE, verbose_name="Departamento")
    
    class Meta:
        verbose_name = "Dueño"
        verbose_name_plural = "Dueños"
    def __init__(self):
        return str(self.name + self.surname)
    