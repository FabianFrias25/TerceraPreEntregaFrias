from django.shortcuts import render
from .models import Equipos, Posiciones


def Inicio(request):
    return render(request, 'AppFutbolArg/Inicio.html')

def equipos_view(request):
    return render(request, 'AppFutbolArg/Equipos.html')

def Fixture(request):
    return render(request, 'AppFutbolArg/Fixture.html')

def posiciones_view(request):
    posiciones = Posiciones.objects.order_by('-puntos', 'PartidosJugados')
    return render(request, 'AppFutbolArg/Posiciones.html', {'posiciones': posiciones})

def ver_equipo(request):
    if "Nombre" in request.GET:
        Nombre = request.GET["Nombre"]
        print(Nombre)
        equipo = Equipos.objects.filter(nombre=Nombre)
        print(equipo)
        return render(request, "AppFutbolArg/getEquipos.html", {"equipo": equipo})
