from django.shortcuts import render
from django.http import HttpResponse
from veranum_web.models import Registro
from veranum_web.models import Habitacion
from veranum_web.models import Reserva
from veranum_web.models import Trabajador

# Create your views here.

def registro_web(request):
    return render(request,"registro.html")

def administracion_web(request):
    return render(request, "administracion.html")

def hotel_s_web(request):
    return render(request, "hotel_s.html")

def hotel_v_web(request):
    return render(request, "hotel_v.html")

def portada_web(request):
    return render(request, "portada.html")

def servicios_web(request):
    return render(request, "servicios.html")

def trabajadores_web(request):
    return render(request,"trabajadores.html")

def reserva_web(request):
    return render(request,"reserva_evento.html")

def iniciar_sesion_web(request):
    return render(request,"iniciar_sesion.html")

def ingresar_habitacion_web(request):
    return render(request,"ingresar_habitacion.html")

def reservacion_web(request):
    return render(request,"reservacion.html")

def informe_trabajador_web(request):
    return render(request,"informe_trabajador.html")

def informe_web(request):
    return render(request,"infomes.html")

def informe_reserva_web(request):
    return render(request,"informe_reservas.html")

def registro(request):
    nombre_aux=request.GET["txt_nombre"]
    apellido_aux=request.GET["txt_apellido"]
    genero_aux=request.GET["txt_genero"]
    fecha_aux=request.GET["fecha"]
    email_aux=request.GET["correo"]
    contrasena_aux=request.GET["contrasena"]
    if len(nombre_aux)>0 and len(apellido_aux)>0 and len(genero_aux)>0 and len(fecha_aux)>0 and len(email_aux)>0 and len(contrasena_aux)>0:
        info = Registro(nombre=nombre_aux,apellido=apellido_aux,genero=genero_aux,fecha_nacimiento=fecha_aux,contraseña=contrasena_aux,correo=email_aux)
        info.save()
        mensaje="Registo completo"
    else:
        mensaje="Registro incorrecto"
    return HttpResponse(mensaje)

def iniciar_sesion(request):
    if request.GET["txt_usuario"] and request.GET["txt_contrasena"]:
        usuario = request.GET["txt_usuario"]
        contrasena = request.GET["txt_contrasena"]
        informacion = Registro(correo__icontains=usuario, contraseña__icontains=contrasena)
        mensaje=("sesion iniciada")
    else:
        mensaje=("El correo o contraseña esta mal.")
    return HttpResponse(mensaje+"<br><h1><a href='/admin/'>Volver al inicio</a></h1>")

def ingresar_habitacion(request):
    nombre_habitacion=request.GET["txt_nombre_habitacion"]
    hotel=request.GET["choice_hotel"]
    habitaciones=request.GET["txt_habitaciones"]
    banos=request.GET["txt_banos"]
    camas=request.GET["txt_camas"]
    imagen=request.GET["img_hotel"]
    descripcion=request.GET["txt_descripcion"]
    precio=request.GET["txt_precio"]
    if len(nombre_habitacion)>0 and len(hotel)>0 and len(habitaciones)>0 and len(banos)>0 and len(camas)>0 and len(imagen)>0 and len(descripcion)>0 and len(precio)>0:
        habitacion=Habitacion(nombre_habitacion=nombre_habitacion, hotel=hotel, habitaciones=habitaciones, banos=banos, camas=camas, foto=imagen, descripcion=descripcion, precio=precio)
        habitacion.save()
        mensaje="Habitacion ingresada"
    else:
        mensaje="Error al ingresar la habitacion"
    return HttpResponse(mensaje)

def reservacion(request):
    ida=request.GET["a"]
    vuelta=request.GET["b"]
    adultos=request.GET["adultos"]
    ninos=request.GET["ninos"]
    hotel=request.GET["categoria"]
    if len(ida)>0 and len(vuelta)>0 and len(adultos)>0 and len(ninos)>0 and len(hotel)>0:
        reserva=Reserva(ida=ida, vuelta=vuelta, adultos=adultos, ninos=ninos, hotel=hotel)
        reserva.save()
        mensaje="Reserva lista"
    else:
        mensaje="error al reserva"
    return HttpResponse(mensaje)

def trabajadores(request):
    nombre=request.GET["txt_nombre"]
    apellido=request.GET["txt_apellido"]
    genero=request.GET["txt_genero"]
    fecha_nacimiento=request.GET["fecha"]
    edad=request.GET["edad"]
    correo=request.GET["correo"]
    cargo=request.GET["cargo"]
    if len(nombre)>0 and len(apellido)>0 and len(genero)>0 and len(fecha_nacimiento)>0 and len(edad)>0 and len(correo)>0 and len(cargo)>0:
        info=Trabajador(nombre=nombre, apellido=apellido, genero=genero, fecha_nacimiento=fecha_nacimiento, edad=edad, correo=correo, cargo=cargo)
        info.save()
        mensaje="informacion ingresada"
    else:
        mensaje="error al ingresar la informacion"
    return HttpResponse(mensaje)

def listar_trabajador(request):
    datos = Trabajador.objects.all()
    return render(request,"informe_trabajador.html",{'informacion':datos})

def listar_reserva(request):
    datos = Reserva.objects.all()
    return render(request,"informe_reservas.html",{'informacion':datos})





