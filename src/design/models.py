"""Gear Design models."""
from django.db import models
from django.contrib.auth.models import User


class Gear(models.Model):
    """Gear Design."""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    fs = models.FloatField(
        'factor de servicio',
        null=True,
    )
    HP = models.FloatField(
        'potencia de motor',
        null=True,
    )
    Np = models.FloatField(
        'dientes del piñón',
        null=True,
    )
    angle = models.FloatField(
        'ángulo',
        null=True,
    )
    Pd = models.FloatField(
        'paso diametral del engrane',
        null=True,
    )
    Wg = models.FloatField(
        'RPMs del engrane',
        null=True,
    )
    Wp = models.FloatField(
        'RPMs del piñón',
        null=True,
    )
    PotD = models.FloatField(
        'potencia de diseño',
        null=True,
    )
    Ng = models.FloatField(
        'dientes del engrane',
        null=True,
    )
    Dp = models.FloatField(
        'paso diametral del piñón',
        null=True,
    )
    Vt = models.FloatField(
        'velocidad tangencial',
        null=True,
    )
    C = models.FloatField(
        'distancia entre centros',
        null=True,
    )
    Ft = models.FloatField(
        'fuerza transmitida',
        null=True,
    )
    F = models.FloatField(
        'ancho de la cara',
        null=True,
    )
    Av = models.IntegerField(
        'Calidad',
        null=True,
    )
    kv = models.FloatField(
        null=True,
    )
    Cpf = models.FloatField(
        'factor de proporción del piñón',
        null=True,
    )

    class Meta:
        verbose_name = "Gear"
        verbose_name_plural = "Gears"

    def __str__(self):
        return 'Gear: {}'.format(self.id)
