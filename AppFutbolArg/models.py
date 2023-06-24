from django.db import models


class Equipos(models.Model):
    nombre = models.CharField(max_length=100)
    fundacion = models.DateField()
    ligasGanadas = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Equipos"


class Fixture(models.Model):
    fecha_dia = models.DateField()
    fecha_hora = models.CharField(max_length=5)
    equipo_local = models.ForeignKey(Equipos, on_delete=models.CASCADE, related_name='fixture_local')
    equipo_visitante = models.ForeignKey(Equipos, on_delete=models.CASCADE, related_name='fixture_visitante')

    def __str__(self):
        return (
            f'{self.fecha_dia} - {self.fecha_hora} - '
            f'{self.equipo_local.nombre} vs {self.equipo_visitante.nombre}'
        )

    class Meta:
        verbose_name_plural = "Fixture"


class Posiciones(models.Model):
    equipo = models.OneToOneField(Equipos, on_delete=models.CASCADE, null=True, blank=True)
    puntos = models.IntegerField()
    partidos_jugados = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.equipo.nombre} - Puntos: {self.puntos} - PJ: {self.partidos_jugados}'

    class Meta:
        verbose_name_plural = "Posiciones"
