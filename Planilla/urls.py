from django.conf.urls import include, url
from django.contrib import admin
from main_app  import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', views.index),
    url(r'^igss/', views.igss_ver),
    url(r'^salario/', views.salario_ver),
    url(r'^empleado/', views.empleado_ver),
    url(r'^planilla/', views.planilla_ver),
    url(r'^planilla_busqueda/', views.planilla_buscar),
    url(r'^AgregarPlanilla/', views.planilla_ver),
    url(r'^bonificacion/', views.bonificacion_ver),
    url(r'^retencion/', views.retencion_ver),
    url(r'^post_igss/', views.igss_ingresar),
    url(r'^post_planilla/(?P<anio>[0-9]{4})/(?P<mes>[0-9]{2})/$', views.planilla_ingreso_datos),
    url(r'^post_retencion/', views.retencion_ingresar),
    url(r'^post_bonificacion/', views.bonificacion_ingresar),
    url(r'^post_salario/', views.salario_ingresar),
    url(r'^post_empleado/', views.empleado_ingresar),
    url(r'^eliminar_igss/(?P<id_igss>[0-9]{2})/$', views.iggs_detalle),
    url(r'^eliminar_retencion/(?P<id_retencion>[0-9])/$', views.eliminar_retencion),
    url(r'^eliminar_salario/(?P<id_salario>[0-9])/$', views.salario_eliminar),
    url(r'^eliminar_bonificacion/(?P<id_bonificacion>[0-9])/$', views.eliminar_bonificacion),
    url(r'^eliminar_empleado/(?P<id_empleado>[0-9]+)/$', views.eliminar_empleado),
    url(r'^eliminar_planilla/(?P<id_planilla>[0-9]+)/$', views.planilla_eliminar),
    url(r'^editar_igss/(?P<id_igss>[0-9]{2})/$', views.editar_igss),
    url(r'^editar_salario/(?P<id_salario>[0-9])/$', views.editar_salario),
    url(r'^editar_empleado/(?P<id_empleado>[0-9]+)/$', views.editar_empleado),
    url(r'^editar_bonificacion/(?P<id_bonificacion>[0-9]+)/$', views.editar_bonificacion),
    url(r'^editar_retencion/(?P<id_retencion>[0-9]+)/$', views.editar_retencion),
    url(r'^editar_planilla/(?P<id_planilla>[0-9]+)/$', views.editar_planilla),
]
