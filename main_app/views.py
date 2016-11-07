from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import Igss,SalarioOrdinario,Empleado,Bonificacion,Retencion,Planilla,PlanillaGenerar
from .forms import IgssForm,SalarioOrdinarioForm,EmpleadoForm,BonificacionForm,RetencionForm,PlanillaForm,PlanillaGenerarForm
import time
import pdb


id_encontrado = 0

def empleado_ingresar(request):
    form = EmpleadoForm(request.POST or None)
    if form.is_valid():
        form_data = form.cleaned_data
        nombre_formulario = form_data.get("nombre_form")
        apellido_formulario = form_data.get("apellido_form")
        fechaInicio_formulario = form_data.get("fechaInicio_form")
        estado_formulario = form_data.get("estado_form")
        fechaInactividad_formulario = form_data.get("fechaInactividad_form")
        obj = Empleado.objects.create(nombre=nombre_formulario,
        apellido=apellido_formulario,
        fechaInicio=fechaInicio_formulario,
        estado=estado_formulario,
        fechaInactividad=fechaInactividad_formulario)
        if request.method=="POST":
            return HttpResponseRedirect('/empleado/')
    return render(request,"post_empleado.html",{'form':form})

def bonificacion_ingresar(request):
    empleados = Empleado.objects.all()
    form = BonificacionForm(request.POST or None, initial={'Bonificacion_form': 0.0})
    if form.is_valid():
        form_data = form.cleaned_data
        cuota_bonificacion_form = form_data.get("Bonificacion_form")
        fechabonificacion_bonificacion_form = form_data.get("fechaBonificacion_form")
        usuario_form = request.POST.get('nombres')
        obj=Bonificacion.objects.create(idEmpleado_id=usuario_form,
        BonificacionCuota=cuota_bonificacion_form,
        fechaBonificacion=fechabonificacion_bonificacion_form)
        if request.method=="POST":
            return HttpResponseRedirect('/bonificacion/')
    return render(request,"post_bonificacion.html",{'form':form,'empleados':empleados})

def igss_ingresar(request):
    form = IgssForm(request.POST or None)
    if form.is_valid():
        form_data = form.cleaned_data
        abc = form_data.get("anio__form")
        cuota = form_data.get("cuota_form")
        obj = Igss.objects.create(anio=abc,cuota_igss=cuota)
        if request.method=="POST":
            return HttpResponseRedirect('/igss/')
    return render(request,"post_igss.html",{'form':form})

def salario_ingresar(request):
    form = SalarioOrdinarioForm(request.POST or None)
    if form.is_valid():
        form_data = form.cleaned_data
        abc = form_data.get("anio__form")
        cuota = form_data.get("cuota_form")
        obj = SalarioOrdinario.objects.create(anio=abc,cuota_salario=cuota)
        if request.method=="POST":
            return HttpResponseRedirect('/salario/')
    return render(request,"post_salario.html",{'form':form})

def retencion_ingresar(request):
    empleados = Empleado.objects.all()
    form = RetencionForm(request.POST or None, initial={'Retencion_form': 0.0})
    if form.is_valid():
        form_data = form.cleaned_data
        cuota_retencion_form = form_data.get("Retencion_form")
        fechaRetencion_retencion_form = form_data.get("fechaRetencion_form")
        usuario_form = request.POST.get('nombres')
        obj=Retencion.objects.create(idEmpleado_id=usuario_form,
        RetencionCuota=cuota_retencion_form,
        fechaRetencion=fechaRetencion_retencion_form)
        if request.method=="POST":
            return HttpResponseRedirect('/retencion/')
    return render(request,"post_retencion.html",{'form':form,
                         'empleados':empleados})

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

def editar_bonificacion(request,id_bonificacion):
    empleados = Empleado.objects.all()
    bonificacion = Bonificacion.objects.get(pk=id_bonificacion)
    form = BonificacionForm(request.POST or None)
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


def editar_empleado(request,id_empleado):
    empleado = Empleado.objects.get(pk=id_empleado)
    form = EmpleadoForm(request.POST or None)
    if form.is_valid():
        form_data = form.cleaned_data
        nombre_empleado_form = form_data.get("nombre_form")
        apellido_empleado_form = form_data.get("apellido_form")
        fechaInicio_empleado_form = form_data.get("fechaInicio_form")
        estado_empleado_form= form_data.get("estado_form")
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

def igss_ver(request):
    igss_lista = Igss.objects.all()
    form = IgssForm()
    return render(request,'igss.html',{'igss_lista':igss_lista,'form':form})

def empleado_ver(request):
    empleado_lista = Empleado.objects.all()
    form = EmpleadoForm()
    return render(request,'empleado.html',{'empleado_lista':empleado_lista,
    'form':form})

def salario_ver(request):
    salario_lista = SalarioOrdinario.objects.all()
    form = SalarioOrdinarioForm()
    return render(request,'salario.html',{'salario_lista':salario_lista,
    'form':form})

def bonificacion_ver(request):
    bonificacion_lista = Bonificacion.objects.all()
    form = BonificacionForm()
    return render(request,'bonificacion.html',{'bonificacion_lista':bonificacion_lista,
    'form':form})

def iggs_detalle(request,id_igss):
    igss = Igss.objects.get(pk=id_igss)
    igss.delete()
    return HttpResponseRedirect('/igss/')

def retencion_ver(request):
    retencion_lista = Retencion.objects.all()
    form = RetencionForm()
    return render(request,'retencion.html',{'retencion_lista':retencion_lista,
    'form':form})

mes_planilla = 0
anio_planilla = 0
planilla_ingreso = []

def datos_generar_planilla(anio,mes):
    mes_planilla= mes
    anio_planilla = anio


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
    datos_generar_planilla(anio_seleccionado,mes_seleccionado)
    if request.method=="POST":
        anios_Igss = Igss.objects.get(anio=anio_seleccionado)
        anios_Salario = SalarioOrdinario.objects.get(anio=anio_seleccionado)
        empleados_anio = Empleado.objects.filter(fechaInicio__year__lte=anio_seleccionado)
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

lista_nueva = []

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

def planilla_ingreso_datos(request,anio,mes):
    anio_planilla = anio
    mes_planilla = mes
    if request.method=="POST":
        anios_Igss = Igss.objects.get(anio=anio_planilla)
        anios_Salario = SalarioOrdinario.objects.get(anio=anio_planilla)
        empleados_anio = Empleado.objects.filter(fechaInicio__year__lte=anio_planilla)
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

def eliminar_empleado(request,id_empleado):
    empleado = Empleado.objects.get(pk=id_empleado)
    empleado.delete()
    return HttpResponseRedirect('/empleado/')

def eliminar_bonificacion(request,id_bonificacion):
    bonificacion = Bonificacion.objects.get(pk=id_bonificacion)
    bonificacion.delete()
    return HttpResponseRedirect('/bonificacion/')

def eliminar_retencion(request,id_retencion):
    retencion = Retencion.objects.get(pk=id_retencion)
    retencion.delete()
    return HttpResponseRedirect('/retencion/')

def salario_eliminar(request,id_salario):
    salario = SalarioOrdinario.objects.get(pk=id_salario)
    salario.delete()
    return HttpResponseRedirect('/salario/')

def planilla_eliminar(request,id_planilla):
    planilla = PlanillaGenerar.objects.get(pk=id_planilla)
    planilla.delete()
    return HttpResponseRedirect('/planilla_busqueda/')

def index(request):
    return render(request,"index.html")

def igss_principal(request):
    return render(request,"igss.html")
