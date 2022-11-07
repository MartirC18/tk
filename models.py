from django.db import models
class Area(models.Model):
    Nombre=models.CharField(max_length=200)
    Descripcion=models.CharField(max_length=200)
    Localizacion=models.CharField(max_length=200)
class Doctor(models.Model):
    Nombre=models.CharField(max_length=200)
    Apellido=models.CharField(max_length=200)
    Area=models.ForeignKey(Area,on_delete=models.CASCADE)

class Paciente(models.Model):
    Nombre=models.CharField(max_length=200)
    Apellido=models.CharField(max_length=200)
    Edad=models.IntegerField
    Sexo=models.CharField(max_length=200)
    Doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)

class Registro(models.Model):
    Paciente=models.CharField(max_length=200)
    Fecha_Ingreso=models.DateField
    Fecha_Salida=models.DateField
    Motivo_de_ingreso=models.CharField(max_length=200)
    Area=models.ForeignKey(Area,on_delete=models.CASCADE)
