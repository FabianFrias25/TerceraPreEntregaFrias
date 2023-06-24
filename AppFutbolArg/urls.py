from django.urls import path
from AppFutbolArg.views import Inicio, ver_equipos, ver_posiciones, ver_fixture, ver_equipo

urlpatterns = [
    path('inicio/', Inicio, name="Inicio"),
    path('equipos/', ver_equipos, name="Equipos"),
    path('posiciones/', ver_posiciones, name="Posiciones"),
    path('fixture/', ver_fixture, name="Fixture"),
    path('getequipo/', ver_equipo, name="ver_equipo"),
]