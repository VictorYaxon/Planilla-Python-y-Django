import time
import datetime, calendar
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.utils.dateparse import parse_date
from .models import Igss,SalarioOrdinario,Empleado,Bonificacion,Retencion,Planilla,PlanillaGenerar
from .forms import IgssForm,SalarioOrdinarioForm,EmpleadoForm,BonificacionForm,RetencionForm,PlanillaForm,PlanillaGenerarForm

mes_planilla = 0
anio_planilla = 0
planilla_ingreso = []
lista_nueva = []

#Funcion para Agregar Empleados
def empleado_ingresar(request):
    form = EmpleadoForm(request.POST or None)
    if form.is_valid():
        form_data = form.cleaned_data
        nombre_formulario = form_data.get("nombre_form")
        apellido_formulario = form_data.get("apellido_form")
        fechaInicio_formulario = form_data.get("fechaInicio_form")
        estado_formulario = request.POST.get('estado')
        fechaInactividad_formulario = form_data.get("fechaInactividad_form")
        obj = Empleado.objects.get_or_create(nombre=nombre_formulario,
        apellido=apellido_formulario,
        fechaInicio=fechaInicio_formulario,
        estado=estado_formulario,
        fechaInactividad=fechaInactividad_formulario)
        if request.method=="POST":
            return HttpResponseRedirect('/empleado/')
    return render(request,"post_empleado.html",{'form':form})

#Funcion para Agregar Bonificacion
def bonificacion_ingresar(request):
    empleados = Empleado.objects.all()
    form = BonificacionForm(request.POST or None, initial={'Bonificacion_form': 0.0})
    if form.is_valid():
        form_data = form.cleaned_data
        cuota_bonificacion_form = form_data.get("Bonificacion_form")
        fechabonificacion_bonificacion_form = form_data.get("fechaBonificacion_form")
        usuario_form = request.POST.get('nombres')
        fecha = fechabonificacion_bonificacion_form
        bonificacion_crear = Bonificacion.objects.filter(fechaBonificacion__month=fecha.month,fechaBonificacion__year=fecha.year,idEmpleado_id=usuario_form)
        bonificacion_crear.exists()
        if bonificacion_crear.exists() == True:
            print ("ya existe un registro")
        else:
            obj=Bonificacion.objects.get_or_create(idEmpleado_id=usuario_form,
            BonificacionCuota=cuota_bonificacion_form,
            fechaBonificacion=fechabonificacion_bonificacion_form)
        if request.method=="POST":
            return HttpResponseRedirect('/bonificacion/')
    return render(request,"post_bonificacion.html",{'form':form,'empleados':empleados})

#Funcion para Ingresar IGSS
def igss_ingresar(request):
    form = IgssForm(request.POST or None)
    if form.is_valid():
        form_data = form.cleaned_data
        abc = form_data.get("anio__form")
        cuota = form_data.get("cuota_form")
        fecha = Igss.objects.filter(anio=abc)
        if fecha.exists()==True:
            print ("ya existe un registro")
        else:
            obj = Igss.objects.get_or_create(anio=abc,cuota_igss=cuota)
        if request.method=="POST":
            return HttpResponseRedirect('/igss/')
    return render(request,"post_igss.html",{'form':form})

#Funcion para Ingresar Salario
def salario_ingresar(request):
    form = SalarioOrdinarioForm(request.POST or None)
    if form.is_valid():
        form_data = form.cleaned_data
        abc = form_data.get("anio__form")
        cuota = form_data.get("cuota_form")
        fecha = SalarioOrdinario.objects.filter(anio=abc)
        if fecha.exists()==True:
            print ("ya existe un registro")
        else:
            obj = SalarioOrdinario.objects.get_or_create(anio=abc,cuota_salario=cuota)
        if request.method=="POST":
            return HttpResponseRedirect('/salario/')
    return render(request,"post_salario.html",{'form':form})

#Funcion para Ingresar Retenciones
def retencion_ingresar(request):
    empleados = Empleado.objects.all()
    form = RetencionForm(request.POST or None, initial={'Retencion_form': 0.0})
    if form.is_valid():
        form_data = form.cleaned_data
        cuota_retencion_form = form_data.get("Retencion_form")
        fechaRetencion_retencion_form = form_data.get("fechaRetencion_form")
        usuario_form = request.POST.get('nombres')
        fecha = fechaRetencion_retencion_form
        retencion_crear = Retencion.objects.filter(fechaRetencion__month=fecha.month,
        fechaRetencion__year=fecha.year,idEmpleado_id=usuario_form)
        retencion_crear.exists()
        if retencion_crear.exists() == True:
            print ("ya existe un registro")
        else:
            obj=Retencion.objects.get_or_create(idEmpleado_id=usuario_form,
            RetencionCuota=cuota_retencion_form,
            fechaRetencion=fechaRetencion_retencion_form)
        if request.method=="POST":
            return HttpResponseRedirect('/retencion/')
    return render(request,"post_retencion.html",{'form':form,
                         'empleados':empleados})

#Funcion para Editar Salario obteniendo id
def editar_salario(request,id_salario):
    salario = SalarioOrdinario.objects.get(pk=id_salario)
    form = SalarioOrdinarioForm(request.POST or None)
    if form.is_valid():
        form_data = form.cleaned_data
        anio_salario_form = form_data.get("anio__form")
        cuota_salario_form = form_data.get("cuota_form")
        salario.cuota_salario = cuota_salario_form
        salario.anio = anio_salario_form
        salario.save()
        if request.method=="POST":
            return HttpResponseRedirect('/salario/')
    return render(request,'editar_salario.html',{'form':form})

#Funcion para Editar Retencion obteniendo id
def editar_retencion(request,id_retencion):
    empleados = Empleado.objects.all()
    retencion = Retencion.objects.get(pk=id_retencion)
    form = RetencionForm(request.POST or None,initial={
    'Retencion_form':retencion.RetencionCuota,
    'fechaRetencion_form':retencion.fechaRetencion})
    if form.is_valid():
        form_data = form.cleaned_data
        cuota_retencion_form = form_data.get("Retencion_form")
        fechaRetencion_retencion_form = form_data.get("fechaRetencion_form")
        usuario_form = request.POST.get('nombres')
        retencion.RetencionCuota=cuota_retencion_form
        retencion.fechaRetencion=fechaRetencion_retencion_form
        retencion.idEmpleado_id=usuario_form
        retencion.save()
        if request.method=="POST":
            return HttpResponseRedirect('/retencion/')
    return render(request,"post_retencion.html",{'form':form,'empleados':empleados})

#Funcion para Editar IGSS obteniendo id
def editar_igss(request,id_igss):
    igss = Igss.objects.get(pk=id_igss)
    form = IgssForm(request.POST or None)
    if form.is_valid():
        form_data = form.cleaned_data
        anio_igss_form = form_data.get("anio__form")
        cuota_igss_form = form_data.get("cuota_form")
        igss.cuota_igss = cuota_igss_form
        igss.anio = anio_igss_form
        igss.save()
        if request.method=="POST":
            return HttpResponseRedirect('/igss/')
    return render(request,"editar_igss.html",{'form':form})

#Funcion para Editar Bonificacion obteniendo id
def editar_bonificacion(request,id_bonificacion):
    empleados = Empleado.objects.all()
    bonificacion = Bonificacion.objects.get(pk=id_bonificacion)
    form = BonificacionForm(request.POST or None,initial={'Bonificacion_form':bonificacion.BonificacionCuota,
    'fechaBonificacion_form':bonificacion.fechaBonificacion,'idEmpleado_id':bonificacion.idEmpleado_id})
    if form.is_valid():
        form_data = form.cleaned_data
        cuota_bonificacion_form = form_data.get("Bonificacion_form")
        fechabonificacion_bonificacion_form = form_data.get("fechaBonificacion_form")
        usuario_form = request.POST.get('nombres')
        bonificacion.idEmpleado_id=usuario_form
        bonificacion.BonificacionCuota = cuota_bonificacion_form
        bonificacion.fechaBonificacion = fechabonificacion_bonificacion_form
        bonificacion.save()
        if request.method=="POST":
            return HttpResponseRedirect('/bonificacion/')
    return render(request,"post_bonificacion.html",{'form':form,'empleados':empleados})

#Funcion para Editar Planilla obteniendo id
def editar_planilla(request,id_planilla):
    planilla = PlanillaGenerar.objects.get(pk=id_planilla)
    form = PlanillaGenerarForm(request.POST or None,
    initial={'empleado_planilla': planilla.empleado_planilla,
        'apellido_planilla': planilla.apellido_planilla,
        'fecha_inicio_planilla': planilla.fecha_inicio_planilla,
        'igss_cuota': planilla.igss_cuota,
        'igss_anio_planilla': planilla.igss_anio_planilla,
        'mes_planilla': planilla.mes_planilla,
        'cuota_salario_planilla': planilla.cuota_salario_planilla,
        'bonificacion_planilla': planilla.bonificacion_planilla,
        'retencion_planilla': planilla.retencion_planilla,
        'sueldoTotal_planilla': planilla.sueldoTotal_planilla,
        'sueldoLiquido_planilla': planilla.sueldoLiquido_planilla })
    if form.is_valid():
        form_data = form.cleaned_data
        planilla.empleado_planilla= form_data.get("empleado_planilla")
        planilla.apellido_planilla= form_data.get("apellido_planilla")
        planilla.fecha_inicio_planilla= form_data.get("fecha_inicio_planilla")
        planilla.igss_cuota= form_data.get("igss_cuota")
        planilla.igss_anio_planilla= form_data.get("igss_anio_planilla")
        planilla.mes_planilla= form_data.get("mes_planilla")
        planilla.cuota_salario_planilla= form_data.get("cuota_salario_planilla")
        planilla.bonificacion_planilla= form_data.get("bonificacion_planilla")
        planilla.retencion_planilla= form_data.get("retencion_planilla")
        sueldoT = float(form_data.get("retencion_planilla"))
        + float(form_data.get("cuota_salario_planilla"))
        + float(form_data.get("bonificacion_planilla"))
        planilla.sueldoTotal_planilla= sueldoT
        sueldoL = sueldoT - float(form_data.get("retencion_planilla"))
        - float(form_data.get("igss_cuota"))
        planilla.sueldoLiquido_planilla= sueldoL
        planilla.save()
    return render(request,"editar_planilla.html",{'form':form})

#Funcion para Editar Empleado obteniendo id
def editar_empleado(request,id_empleado):
    empleado = Empleado.objects.get(pk=id_empleado)
    form = EmpleadoForm(request.POST or None,initial={'nombre_form':empleado.nombre,
    'apellido_form':empleado.apellido,'fechaInicio_form':empleado.fechaInicio,
    'fechaInactividad_form':empleado.fechaInactividad})
    if form.is_valid():
        form_data = form.cleaned_data
        nombre_empleado_form = form_data.get("nombre_form")
        apellido_empleado_form = form_data.get("apellido_form")
        fechaInicio_empleado_form = form_data.get("fechaInicio_form")
        estado_empleado_form = request.POST.get('estado')
        fechaInactividad_empleado_form = form_data.get("fechaInactividad_form")
        empleado.nombre = nombre_empleado_form
        empleado.apellido = apellido_empleado_form
        empleado.fechaInicio = fechaInicio_empleado_form
        empleado.estado = estado_empleado_form
        empleado.fechaInactividad = fechaInactividad_empleado_form
        empleado.save()
        if request.method=="POST":
            return HttpResponseRedirect('/empleado/')
    return render(request,"editar_empleado.html",{'form':form})

#Funcion para Obtener lista de Igss de la base de datos
def igss_ver(request):
    igss_lista = Igss.objects.all()
    form = IgssForm()
    return render(request,'igss.html',{'igss_lista':igss_lista,'form':form})

#Funcion para Obtener lista de Empleados de la base de datos
def empleado_ver(request):
    empleado_lista = Empleado.objects.all()
    form = EmpleadoForm()
    return render(request,'empleado.html',{'empleado_lista':empleado_lista,
    'form':form})

#Funcion para Obtener lista de Salarios de la base de datos
def salario_ver(request):
    salario_lista = SalarioOrdinario.objects.all()
    form = SalarioOrdinarioForm()
    return render(request,'salario.html',{'salario_lista':salario_lista,
    'form':form})

#Funcion para Obtener lista de Bonificaciones de la base de datos
def bonificacion_ver(request):
    bonificacion_lista = Bonificacion.objects.all()
    form = BonificacionForm()
    return render(request,'bonificacion.html',{'bonificacion_lista':bonificacion_lista,
    'form':form})

#Funcion para Eliminar IGSS de la base de datos obteniendo el ID
def iggs_detalle(request,id_igss):
    igss = Igss.objects.get(pk=id_igss)
    igss.delete()
    return HttpResponseRedirect('/igss/')

#Funcion Para obtener lista de retenciones de la base de datos
def retencion_ver(request):
    retencion_lista = Retencion.objects.all()
    form = RetencionForm()
    return render(request,'retencion.html',{'retencion_lista':retencion_lista,
    'form':form})

#Funcion Para obtener lista de Empleados,IGSS y salario ordinario de la DB
def planilla_ver(request):
    form = PlanillaForm()
    anios = []
    for i in range(1999,int(time.strftime("%Y"))):
        i = i + 1
        anios.append(i)
    mes_seleccionado= request.POST.get('meses')
    anio_seleccionado= request.POST.get('nombres')
    mes_planilla = mes_seleccionado
    anio_planilla = anio_seleccionado
    if request.method=="POST":
        anios_Igss = Igss.objects.get(anio=anio_seleccionado)
        anios_Salario = SalarioOrdinario.objects.get(anio=anio_seleccionado)
        empleados_anio = Empleado.objects.filter(fechaInicio__year__lte=anio_seleccionado,estado="Activo")
        for empleado in empleados_anio:
            retencion_planilla = empleado.retencion_set.filter(
            fechaRetencion__year__lte=anio_seleccionado,
            fechaRetencion__month__lte=mes_seleccionado,
            idEmpleado=empleado.id)[:1]
            bonificacion_planilla = empleado.bonificacion_set.filter(
            fechaBonificacion__year__lte=anio_seleccionado,
            fechaBonificacion__month__lte=mes_seleccionado,
            idEmpleado=empleado.id)[:1]
            for item in bonificacion_planilla:
                empleado.bono = item.BonificacionCuota
                if empleado.bono == "Unknown":
                    empleado.bono = 0.0
                    print (empleado.bono)
                empleado.totalSueldo = float(anios_Salario.cuota_salario) + float(empleado.bono)
                empleado.sueldoLiquido = empleado.totalSueldo - float(anios_Igss.cuota_igss)
            for items in retencion_planilla:
                empleado.ret = items.RetencionCuota
                if empleado.ret == "Unknown":
                    empleado.ret = 0.0
                empleado.totalSueldo += float(empleado.ret)
                empleado.sueldoLiquido

        return render(request,'planillatabla.html',
                {'mes_seleccionado':mes_seleccionado,
                'anios_Igss':anios_Igss,'empleados_anio':empleados_anio,
                'anios_Salario':anios_Salario,
                'bonificacion_planilla':bonificacion_planilla,
                'anio_seleccionado':anio_seleccionado,})
    return render(request,'planilla.html',{'anio_planilla':anio_planilla,
    'anios_lista':anios,
    'form':form,'mes_seleccionado':mes_seleccionado,'anio_seleccionado':anio_seleccionado})

#Filtrar planillas Generadas por Anio y mes
def planilla_buscar(request):
    anios = []
    for i in range(1999,int(time.strftime("%Y"))):
        i = i + 1
        anios.append(i)
    mes_seleccionado= request.POST.get('meses')
    anio_seleccionado= request.POST.get('nombres')
    planillasGeneradas_lista = PlanillaGenerar.objects.filter(
    mes_planilla=mes_seleccionado,
    igss_anio_planilla=anio_seleccionado)
    if request.method=="POST":
        form = PlanillaGenerarForm()
        return render(request,'planilla_tabla_buscar.html',
                {'mes_seleccionado':mes_seleccionado,
                'planillasGeneradas_lista':planillasGeneradas_lista,
                'anio_seleccionado':anio_seleccionado,})
    return render(request,
                         'planillabuscar.html',{'anio_planilla':anio_planilla,
                         'anios_lista':anios,
                         'mes_seleccionado':mes_seleccionado,
                         'anio_seleccionado':anio_seleccionado})

#Funcion para obtener la lista y agregarlas a la base de datos
def planilla_datos(x,igss,salario,mes,anio):
    form = PlanillaForm()
    for planilla in x:
        nombre = planilla.nombre
        apellido = planilla.apellido
        fecha_ini = planilla.fechaInicio
        anio_igss = anio
        cuota_igs= igss
        mes_select = mes
        anio_salario_cuota = salario
        bono = planilla.bono
        retencion = planilla.ret
        totalSueldo = planilla.totalSueldo
        sueldoLiquido = planilla.sueldoLiquido
        lista_nueva.append(planilla)
        obj = PlanillaGenerar.objects.get_or_create(empleado_planilla=nombre,
            apellido_planilla=apellido,
            fecha_inicio_planilla=fecha_ini,
            igss_anio_planilla = anio_igss,
            igss_cuota = cuota_igs,
            mes_planilla=mes_select,
            cuota_salario_planilla = anio_salario_cuota,
            bonificacion_planilla = bono,
            retencion_planilla = retencion,
            sueldoTotal_planilla = totalSueldo,
            sueldoLiquido_planilla =  sueldoLiquido
            )
        HttpResponseRedirect('/index/')

#Funcion que recibe anio y mes, similar a ver planilla pero invoca funcion datos_generar_planilla
def planilla_ingreso_datos(request,anio,mes):
    anio_planilla = anio
    mes_planilla = mes
    if request.method=="POST":
        anios_Igss = Igss.objects.get(anio=anio_planilla)
        anios_Salario = SalarioOrdinario.objects.get(anio=anio_planilla)
        empleados_anio = Empleado.objects.filter(fechaInicio__year__lte=anio_planilla,estado="Activo")
        for empleado in empleados_anio:
            retencion_planilla = empleado.retencion_set.filter(
                                    fechaRetencion__year__lte=anio_planilla,
                                    fechaRetencion__month__lte=mes_planilla,
                                    idEmpleado=empleado.id)[:1]
            bonificacion_planilla = empleado.bonificacion_set.filter(
                                    fechaBonificacion__year__lte=anio_planilla,
                                    fechaBonificacion__month__lte=mes_planilla,
                                    idEmpleado=empleado.id)[:1]
            for item in bonificacion_planilla:
                empleado.bono = item.BonificacionCuota
                empleado.totalSueldo = float(anios_Salario.cuota_salario) + float(empleado.bono)
                empleado.sueldoLiquido = empleado.totalSueldo - float(anios_Igss.cuota_igss)
            for items in retencion_planilla:
                empleado.ret = items.RetencionCuota
                empleado.totalSueldo += float(empleado.ret)
                empleado.sueldoLiquido
                planilla_ingreso.append(empleado)
                planilla_datos(planilla_ingreso,anios_Igss.cuota_igss
                                               ,anios_Salario.cuota_salario
                                               ,mes_planilla
                                               ,anio_planilla)
        if request.method=="POST":
            print ('hola')
        return HttpResponseRedirect('/planilla/')
    return render(request,'post_planilla.html')

def planilla_ingresar(request):
    mes_seleccionado= request.POST.get('meses')
    anio_seleccionado= request.POST.get('nombres')
    if request.method=="POST":
        anios_Igss = Igss.objects.get(anio=anio_seleccionado)
        anios_Salario = SalarioOrdinario.objects.get(anio=anio_seleccionado)
        empleados_anio = Empleado.objects.filter(
                        fechaInicio__year__lte=anio_seleccionado)
        for empleado in empleados_anio:
            retencion_planilla = empleado.retencion_set.filter(
                                fechaRetencion__year__lte=anio_seleccionado,
                                fechaRetencion__month__lte=mes_seleccionado,
                                idEmpleado=empleado.id)[:1]
            bonificacion_planilla = empleado.bonificacion_set.filter(
                                    fechaBonificacion__year__lte=anio_seleccionado,
                                    fechaBonificacion__month__lte=mes_seleccionado,
                                    idEmpleado=empleado.id)[:1]
            for item in bonificacion_planilla:
                empleado.bono = item.BonificacionCuota
                empleado.totalSueldo = float(anios_Salario.cuota_salario)+ float(empleado.bono)
                empleado.sueldoLiquido = empleado.totalSueldo- float(anios_Igss.cuota_igss)
            for items in retencion_planilla:
                empleado.ret = items.RetencionCuota
                empleado.totalSueldo += float(empleado.ret)
                empleado.sueldoLiquido

        return render(request,'planillatabla.html',
                {'mes_seleccionado':mes_seleccionado,
                'anios_Igss':anios_Igss,'empleados_anio':empleados_anio,
                'anios_Salario':anios_Salario,
                'bonificacion_planilla':bonificacion_planilla,
                'anio_seleccionado':anio_seleccionado,'lista':lista})

#Funcion eliminar empleado de la base de datos
def eliminar_empleado(request,id_empleado):
    empleado = Empleado.objects.get(pk=id_empleado)
    empleado.delete()
    return HttpResponseRedirect('/empleado/')

#Funcion bonificacion de la base de datos
def eliminar_bonificacion(request,id_bonificacion):
    bonificacion = Bonificacion.objects.get(pk=id_bonificacion)
    bonificacion.delete()
    return HttpResponseRedirect('/bonificacion/')

#Funcion eliminar retencion de la base de datos
def eliminar_retencion(request,id_retencion):
    retencion = Retencion.objects.get(pk=id_retencion)
    retencion.delete()
    return HttpResponseRedirect('/retencion/')

#Funcion eliminar salario de la base de datos
def salario_eliminar(request,id_salario):
    salario = SalarioOrdinario.objects.get(pk=id_salario)
    salario.delete()
    return HttpResponseRedirect('/salario/')

#Funcion eliminar planilla de la base de datos
def planilla_eliminar(request,id_planilla):
    planilla = PlanillaGenerar.objects.get(pk=id_planilla)
    planilla.delete()
    return HttpResponseRedirect('/planilla_busqueda/')

#Funcion menu para la pagina inicial
def index(request):
    return render(request,"index.html")

#Funcion para listar IGSS
def igss_principal(request):
    return render(request,"igss.html")
