from django.db import models



class Homeowner(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, verbose_name="Nombre")
    surname = models.CharField(max_length=200, verbose_name="Apellido")
    phone = models.CharField(max_length=200, verbose_name="Telefono")
    email = models.EmailField(default="No tiene")
   
    
    class Meta:
        verbose_name = "Dueño"
        verbose_name_plural = "Dueños"
    def __str__(self):
       return self.surname
    