from django.db import models



class Homeowner(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, verbose_name="Nombre")
    surname = models.CharField(max_length=200, verbose_name="Apellido")
    phone = models.CharField(max_length=200, verbose_name="Telefono", blank=True, null=True)
    email = models.EmailField(default="abc@gmail.com", blank=True, null=True)
   
    
    class Meta:
        verbose_name = "Dueño"
        verbose_name_plural = "Dueños"
    def __str__(self):
       return self.surname
    