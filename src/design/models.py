"""Gear Design models."""
from django.db import models
from django.contrib.auth.models import User


class Gear(models.Model):
    """Gear Design."""

    Np_CHOICES = (
        (12.0, 12.0),
        (18.0, 18.0),
        (32.0, 32.0),
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    fs = models.FloatField(
        'Factor de servicio',
        null=True,
    )
    HP = models.FloatField(
        'Potencia de motor',
        null=True,
    )
    Np = models.FloatField(
        'Dientes del piñón',
        choices=Np_CHOICES,
        null=True,
    )
    angle = models.FloatField(
        'Ángulo',
        null=True,
    )
    Pd = models.FloatField(
        'Paso diametral',
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
        'Potencia de diseño',
        null=True,
    )
    Ng = models.FloatField(
        'Dientes del engrane',
        null=True,
    )
    Dp = models.FloatField(
        'Diametro de paso del piñón',
        null=True,
    )
    Dg = models.FloatField(
        'Diametro de paso del engrane',
        null=True,
    )
    Vt = models.FloatField(
        'Velocidad tangencial',
        null=True,
    )
    C = models.FloatField(
        'Distancia entre centros',
        null=True,
    )
    Ft = models.FloatField(
        'Fuerza transmitida',
        null=True,
    )
    F = models.FloatField(
        'Ancho de la cara',
        null=True,
    )
    Av = models.IntegerField(
        'Calidad',
        null=True,
    )
    kv = models.FloatField(
        'Factor dinámico',
        null=True,
    )
    kb = models.FloatField(
        'Factor de espesor de la corona',
        default=1.0,
    )
    kr = models.FloatField(
        'Factor de confiabilidad',
        default=1.0,
    )
    Cpf = models.FloatField(
        'Factor de proporción del piñón',
        null=True,
    )
    addendum = models.FloatField(
        'Addendum',
        null=True,
    )
    dedendum = models.FloatField(
        'Dedendum',
        null=True,
    )
    clair = models.FloatField(
        'Claro',
        null=True,
    )
    Dep = models.FloatField(
        'Diametro exterior del piñón',
        null=True,
    )
    Deg = models.FloatField(
        'Diametro exterior del engrane',
        null=True,
    )
    Drp = models.FloatField(
        'Diametro de raíz del piñón',
        null=True,
    )
    Drg = models.FloatField(
        'Diametro de raíz del engrane',
        null=True,
    )
    depth_total = models.FloatField(
        'Profunidad total',
        null=True,
    )
    work_depth = models.FloatField(
        'Profunidad de trabajo',
        null=True,
    )
    t = models.FloatField(
        'Espesor de diente',
        null=True,
    )

    class Meta:
        verbose_name = "Gear"
        verbose_name_plural = "Gears"

    def __str__(self):
        return 'Gear: {}'.format(self.id)
