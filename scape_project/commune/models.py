
from django.contrib.gis.db import models


class Commune(models.Model):
    insee = models.CharField(max_length=6)
    nom = models.CharField(max_length=255)
    part75_plus = models.IntegerField(default=None, blank=True, null=True)
    evo75_plus = models.IntegerField(default=None, blank=True, null=True)
    parretrait = models.IntegerField(default=None, blank=True, null=True)
    evo65seuls = models.IntegerField(default=None, blank=True, null=True)
    mediane = models.IntegerField(default=None, blank=True, null=True)
    mediane75 = models.IntegerField(default=None, blank=True, null=True)
    partT5 = models.IntegerField(default=None, blank=True, null=True)
    partmaison = models.IntegerField(default=None, blank=True, null=True)
    a60ascenseu = models.IntegerField(default=None, blank=True, null=True)
    popasdense = models.IntegerField(default=None, blank=True, null=True)
    partT5rp = models.IntegerField(default=None, blank=True, null=True)
    diffrevenu = models.IntegerField(default=None, blank=True, null=True)
    cadres55an = models.IntegerField(default=None, blank=True, null=True)
    s15_19seuls = models.IntegerField(default=None, blank=True, null=True)
    s20_24seuls = models.IntegerField(default=None, blank=True, null=True)
    t1529total = models.IntegerField(default=None, blank=True, null=True)
    part1524se = models.IntegerField(default=None, blank=True, null=True)
    atlasnb = models.IntegerField(default=None, blank=True, null=True)
    placetud = models.IntegerField(default=None, blank=True, null=True)
    densitplac = models.IntegerField(default=None, blank=True, null=True)
    evojeunes = models.FloatField(default=None, blank=True, null=True)
    T1T2 = models.IntegerField(default=None, blank=True, null=True)
    locataires = models.IntegerField(default=None, blank=True, null=True)
    geom = models.MultiPolygonField(spatial_index=True)  # stocke la géométrie du shapefile

    def __str__(self):
        return f"{self.nom}, {self.id}"

    class Meta:
        ordering = ("nom", "pk")
