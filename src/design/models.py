"""Gear Design models."""
from django.db import models
from django.urls import reverse
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
    P = models.FloatField(
        'Paso circular',
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
    Cp = models.FloatField(
        'Constante de elasticidad',
        null=True,
    )
    Av = models.IntegerField(
        'Calidad',
        null=True,
    )
    Jp = models.FloatField(
        'Factor geométrico del piñón',
        null=True,
    )
    Jg = models.FloatField(
        'Factor geométrico del engrane',
        null=True,
    )
    I = models.FloatField(
        'Factor geométrico',
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
    SF = models.FloatField(
        'Factor de seguridad',
        default=1.0,
    )
    kr = models.FloatField(
        'Factor de confiabilidad',
        default=1.0,
    )
    ks = models.FloatField(
        'Factor de tamaño',
        null=True,
    )
    km = models.FloatField(
        'Factor de distribución de carga',
        null=True,
    )
    Cpf = models.FloatField(
        'Factor de proporción del piñón',
        null=True,
    )
    Cma = models.FloatField(
        'Factor de alineación',
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
    Dbp = models.FloatField(
        'Diametro de círculo base del piñón',
        null=True,
    )
    Dbg = models.FloatField(
        'Diametro de círculo base del engrane',
        null=True,
    )
    Ep = models.FloatField(
        'Módulo de elasticidad del piñón',
        null=True,
    )
    Eg = models.FloatField(
        'Módulo de elasticidad del engrane',
        null=True,
    )
    Vp = models.FloatField(
        'Cte de poison del piñón',
        null=True,
    )
    Vg = models.FloatField(
        'Cte de poison del engrane',
        null=True,
    )
    hrs = models.FloatField(
        'Horas de trabajo por día',
        null=True,
    )
    L = models.FloatField(
        'Vida del componente',
        null=True,
    )
    q = models.FloatField(
        'Aplicaciones de carga por rev',
        null=True,
    )
    Ncp = models.FloatField(
        'Vida del piñón en ciclos',
        null=True,
    )
    Ncg = models.FloatField(
        'Vida del engrane en ciclos',
        null=True,
    )
    Ynp = models.FloatField(
        'Factor de fuerza por estres del piñón',
        null=True,
    )
    Znp = models.FloatField(
        'Factor de resistencia por picaduras del piñón',
        null=True,
    )
    Yng = models.FloatField(
        'Factor de fuerza por estres del engrane',
        null=True,
    )
    Zng = models.FloatField(
        'Factor de resistencia por picaduras del engrane',
        null=True,
    )
    Stp = models.FloatField(
        'Esfuerzo de flexión en el piñón',
        null=True,
    )
    Stg = models.FloatField(
        'Esfuerzo de flexión en el engrane',
        null=True,
    )
    Satp = models.FloatField(
        'Esfuerzo de flexión ajustado en el piñón',
        null=True,
    )
    Satg = models.FloatField(
        'Esfuerzo de flexión ajustado en el engrane',
        null=True,
    )
    Sc = models.FloatField(
        'Esfuerzo de contacto',
        null=True,
    )
    Sacp = models.FloatField(
        'Esfuerzo de contacto ajustado en el piñón',
        null=True,
    )
    Sacg = models.FloatField(
        'Esfuerzo de contacto ajustado en el engrane',
        null=True,
    )

    class Meta:
        verbose_name = "Gear"
        verbose_name_plural = "Gears"

    def __str__(self):
        return 'Engrane: {}'.format(self.id)

    def get_absolute_url(self):
        return reverse('design:gear', args=[self.user.id, self.id])
