from django.shortcuts import render
from .models import Equipos


def Inicio(request):
    return render(request, 'AppFutbolArg/Inicio.html')

def equipos_view(request):
    return render(request, 'AppFutbolArg/Equipos.html')

def Fixture(request):
    return render(request, 'AppFutbolArg/Fixture.html')

def Posiciones(request):
    return render(request, 'AppFutbolArg/Posiciones.html')

def ver_equipo(request):
    if "Nombre" in request.GET:
        Nombre = request.GET["Nombre"]
        print(Nombre)
        equipo = Equipos.objects.filter(nombre=Nombre)
        print(equipo)
        return render(request, "AppFutbolArg/getEquipos.html", {"equipo": equipo})
