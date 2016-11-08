from django.db import models
from django.utils.encoding import python_2_unicode_compatible
# Create your models here.
class Usuarios(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fechaInicio = models.DateField()
    estado = models.CharField(max_length=100)
    fechaInactividad = models.DateField(null=True)

    def __str__(self):
        return self.nombre

class Bonificacion(models.Model):
    idEmpleado = models.ForeignKey(Empleado,on_delete=models.CASCADE)
    BonificacionCuota = models.FloatField()
    fechaBonificacion = models.DateField()

    def __str__(self):
        return str(self.BonificacionCuota)


class Retencion(models.Model):
    idEmpleado = models.ForeignKey(Empleado)
    RetencionCuota = models.FloatField()
    fechaRetencion = models.DateField()

    def __str__(self):
        return str(self.RetencionCuota) + str(self.idEmpleado)

class Igss(models.Model):
    anio = models.CharField(max_length=100)
    cuota_igss = models.CharField(max_length=100)

    def __str__(self):
        return self.anio


class SalarioOrdinario(models.Model):
    anio = models.CharField(max_length=100)
    cuota_salario = models.CharField(max_length=100)

class Planilla(models.Model):
    anio = models.CharField(max_length=100)
    mes = models.CharField(max_length=100)

class PlanillaGenerar(models.Model):
    empleado_planilla = models.CharField(max_length=100)
    apellido_planilla = models.CharField(max_length=100)
    fecha_inicio_planilla = models.CharField(max_length=100)
    igss_anio_planilla  = models.CharField(max_length=100)
    igss_cuota  = models.CharField(max_length=100)
    mes_planilla = models.CharField(max_length=100)
    cuota_salario_planilla  = models.CharField(max_length=100)
    bonificacion_planilla = models.CharField(max_length=100,null=True)
    retencion_planilla = models.CharField(max_length=100,null=True)
    sueldoTotal_planilla  = models.CharField(max_length=100)
    sueldoLiquido_planilla  = models.CharField(max_length=100)

    def __str__(self):
        return self.empleado_planilla,self.apellido_planilla,self.fecha_inicio_planilla,self.igss_anio_planilla
