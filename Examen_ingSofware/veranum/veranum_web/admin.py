from django.contrib import admin

# Register your models here.
from veranum_web.models import Registro
from veranum_web.models import Habitacion
from veranum_web.models import Reserva
from veranum_web.models import Trabajador
admin.site.register(Registro)
admin.site.register(Habitacion)
admin.site.register(Reserva)
admin.site.register(Trabajador)