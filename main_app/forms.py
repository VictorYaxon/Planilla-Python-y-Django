from django import forms
from .models import Igss,SalarioOrdinario,Empleado,Bonificacion

class IgssForm(forms.Form):
    anio__form = forms.CharField(label ="ano",max_length=100)
    cuota_form = forms.CharField(label="cuota",max_length=100)

class SalarioOrdinarioForm(forms.Form):
    anio__form = forms.CharField(label ="ano",max_length=100)
    cuota_form = forms.CharField(label="cuota",max_length=100)

class EmpleadoForm(forms.Form):
    nombre_form = forms.CharField(label ="Nombre",max_length=100)
    apellido_form = forms.CharField(label ="Apellido",max_length=100)
    fechaInicio_form = forms.DateField(label ="Fecha Inicio")
    estado_form = forms.CharField(label ="Estado",max_length=100)
    fechaInactividad_form = forms.DateField(label="Fecha Inactividad",required=False)

class BonificacionForm(forms.Form):
    Bonificacion_form = forms.FloatField(label = "Cuota Bonificacion")
    fechaBonificacion_form = forms.DateField(label = "Fecha Bonificacion")

class RetencionForm(forms.Form):
    Retencion_form = forms.FloatField(label="Cuota Retencion")
    fechaRetencion_form = forms.DateField(label = "Fecha Retencion")

class PlanillaForm(forms.Form):
    pass

class PlanillaGenerarForm(forms.Form):
    empleado_planilla = forms.CharField(label="Nombre",max_length=100,disabled=True)
    apellido_planilla = forms.CharField(label="Apellido",max_length=100,disabled=True)
    fecha_inicio_planilla = forms.CharField(label="Fecha Inicio",max_length=100,disabled=True)
    igss_anio_planilla  = forms.CharField(label="Anio",max_length=100,disabled=True)
    igss_cuota  = forms.CharField(label="Cuota IGSS",max_length=100)
    mes_planilla = forms.CharField(label="Mes",max_length=100,disabled=True)
    cuota_salario_planilla  = forms.CharField(label="Cuota Salario Ordinario",max_length=100)
    bonificacion_planilla = forms.CharField(label="Bonificacion",max_length=100,required=False)
    retencion_planilla = forms.CharField(label="Retencion",max_length=100,required=False)
    sueldoTotal_planilla  = forms.CharField(label="Sueldo Total",max_length=100,disabled=True)
    sueldoLiquido_planilla  = forms.CharField(label="Sueldo Liquido",max_length=100,disabled=True)