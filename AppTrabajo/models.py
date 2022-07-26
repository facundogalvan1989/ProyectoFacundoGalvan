from distutils.command.upload import upload
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User

class Gerente(models.Model):

    nombre = models.CharField(max_length=30)
    legajo = models.IntegerField(max_length=30)
    fecha_ingreso = models.DateField()

    def __str__(self):
        return f"Nombre: {self.nombre} - Legajo: {self.legajo} - Fecha ingreso: {self.fecha_ingreso}"   

class Vendedor(models.Model):

    nombre = models.CharField(max_length=30)
    legajo = models.IntegerField(max_length=30)
    fecha_ingreso = models.DateField()

    def __str__(self):
        return f"Nombre: {self.nombre} - Legajo: {self.legajo} - Fecha ingreso: {self.fecha_ingreso}"       

class Expedicionista(models.Model):

    nombre = models.CharField(max_length=30)
    legajo = models.IntegerField(max_length=30)
    fecha_ingreso = models.DateField()    

    def __str__(self):
        return f"Nombre: {self.nombre} - Legajo: {self.legajo} - Fecha ingreso: {self.fecha_ingreso}"  

class Avatar(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)
