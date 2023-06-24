from django.urls import path
from AppFutbolArg.views import Inicio, equipos_view, posiciones_view, Fixture, ver_equipo

urlpatterns = [
    path('inicio/', Inicio, name="Inicio"),
    path('equipos/', equipos_view, name="Equipos"),
    path('posiciones/', posiciones_view, name="Posiciones"),
    path('fixture/', Fixture, name="Fixture"),
    path('getequipo/', ver_equipo, name="ver_equipo"),
]