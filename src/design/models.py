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
        blank=True,
        null=True,
    )
    HP = models.FloatField(
        'potencia de motor',
        blank=True,
        null=True,
    )
    Np = models.FloatField(
        'dientes del piñón',
        blank=True,
        null=True,
    )
    angle = models.FloatField(
        'ángulo',
        blank=True,
        null=True,
    )
    Pd = models.FloatField(
        'paso diametral del engrane',
        blank=True,
        null=True,
    )
    Wg = models.FloatField(
        'RPMs del engrane',
        blank=True,
        null=True,
    )
    Wp = models.FloatField(
        'RPMs del piñón',
        blank=True,
        null=True,
    )
    PotD = models.FloatField(
        'potencia de diseño',
        blank=True,
        null=True,
    )
    Ng = models.FloatField(
        'dientes del engrane',
        blank=True,
        null=True,
    )
    Dp = models.FloatField(
        'paso diametral del piñón',
        blank=True,
        null=True,
    )
    Vt = models.FloatField(
        'velocidad tangencial',
        blank=True,
        null=True,
    )
    C = models.FloatField(
        'distancia entre centros',
        blank=True,
        null=True,
    )
    Ft = models.FloatField(
        'fuerza transmitida',
        blank=True,
        null=True,
    )
    F = models.FloatField(
        'ancho de la cara',
        blank=True,
        null=True,
    )
    Av = models.IntegerField(
        'Calidad',
        blank=True,
        null=True,
    )
    kv = models.FloatField(
        blank=True,
        null=True,
    )
    Cpf = models.FloatField(
        'factor de proporción del piñón',
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Gear"
        verbose_name_plural = "Gears"

    def __str__(self):
        return 'Gear: {}'.format(self.id)
