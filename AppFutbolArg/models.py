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
    dia = models.DateField()
    hora = models.CharField(max_length=5)
    local = models.ForeignKey(Equipos, on_delete=models.CASCADE, related_name='fixture_local')
    visitante = models.ForeignKey(Equipos, on_delete=models.CASCADE, related_name='fixture_visitante')

    def __str__(self):
        return (
            f'{self.dia} - {self.hora} - '
            f'{self.local.nombre} vs {self.visitante.nombre}'
        )

    class Meta:
        verbose_name_plural = "Fixture"


class Posiciones(models.Model):
    equipo = models.OneToOneField(Equipos, on_delete=models.CASCADE, null=True, blank=True)
    puntos = models.IntegerField()
    PartidosJugados = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.equipo.nombre} - Puntos: {self.puntos} - PJ: {self.PartidosJugados}'

    class Meta:
        verbose_name_plural = "Posiciones"
