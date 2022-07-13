"""veranum URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from veranum_web import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registro_web/',views.registro_web),
    path('registrarse/',views.registro),
    path('reserva_evento/',views.reserva_web),
    path('iniciar_sesion_web/',views.iniciar_sesion_web),
    path('inicio_sesion/',views.iniciar_sesion),
    path('ingresar_habitacion_web/',views.ingresar_habitacion_web),
    path('ingresar_habitacion/',views.ingresar_habitacion),
    path('reservacion_web/',views.reservacion_web),
    path('reservacion/',views.reservacion),
    path('administracion_web/',views.administracion_web),
    path('hotel_s_web/',views.hotel_s_web),
    path('hotel_v_web/',views.hotel_v_web),
    path('portada_web/',views.portada_web),
    path('servicios_web/',views.servicios_web),
    path('trabajadores_web/',views.trabajadores_web),
    path('trabajadores/',views.trabajadores),
    path('informe_trabajador_web/',views.informe_trabajador_web),
    path('informe_trabajador/',views.listar_trabajador),
    path('informes_web/',views.informe_web),
    path('informe_reserva_web/',views.informe_reserva_web),
    path('informe_reserva/',views.listar_reserva),
]

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

