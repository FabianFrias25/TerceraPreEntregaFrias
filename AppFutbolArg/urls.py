from django.urls import path
from AppFutbolArg.views import Inicio, equipos_view, Posiciones, Fixture, ver_equipo

urlpatterns = [
    path('inicio/', Inicio, name="Inicio"),
    path('equipos/', equipos_view, name="Equipos"),
    path('posiciones/', Posiciones, name="Posiciones"),
    path('fixture/', Fixture, name="Fixture"),
    path('getequipo/', ver_equipo, name="ver_equipo"),
]