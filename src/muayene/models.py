# -*- coding: utf-8 -*-

import datetime

from django.core.urlresolvers import reverse
from django.utils import timezone
from django.db import models

from hasta.models import Hasta


class Muayene(models.Model):
    hasta = models.ForeignKey(Hasta)
    tarih = models.DateField(default=timezone.now, editable=False)
    yakinma = models.TextField(max_length=255, blank=True)
    kullandigi_ilaclar = models.TextField(max_length=512, blank=True)
    baki = models.TextField(max_length=255, blank=True)
    ontani_tani = models.TextField(max_length=255, blank=True)
    oneri_gorusler = models.TextField(max_length=255, blank=True)
    ozel_notlar = models.TextField(max_length=255, blank=True)

    class Meta:
        get_latest_by = "tarih"

    def __str__(self):
        return '{}-{}-{}'.format(self.pk, self.hasta, self.tarih)

    def get_absolute_url(self):
        return reverse('muayene:detail', kwargs={'pk': self.pk})

    def was_today(self):
        return self.tarih == datetime.date.today()


class Ilac(models.Model):
    ad = models.CharField(max_length=30)
    bilgi = models.CharField(max_length=30, blank=True, null=True)
    kullanim = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.ad)


class ReceteIlac(models.Model):
    ilac = models.ForeignKey(Ilac)
    kullanim = models.CharField(max_length=30)
    kutu = models.IntegerField(default=1)

    def __str__(self):
        return '{}-{}-{}'.format(self.ilac, self.kullanim, self.kutu)


class Recete(models.Model):
    hasta = models.ForeignKey(Hasta)
    muayene = models.ForeignKey(Muayene)
    tarih = models.DateField(default=timezone.now, editable=False)
    ilaclar = models.ManyToManyField(ReceteIlac)

    def __str__(self):
        return '{}-{}-{}'.format(self.pk, self.hasta, self.tarih)


class Rapor(models.Model):
    hasta = models.ForeignKey(Hasta)
    muayene = models.ForeignKey(Muayene)
    tarih = models.DateField(default=timezone.now, editable=False)
    tani = models.CharField(max_length=255)
    gun = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return '{}-{}-{}'.format(self.pk, self.hasta, self.tarih)


class Laboratuvar(models.Model):
    ad = models.CharField(max_length=30)

    def __str__(self):
        return '{}'.format(self.ad)


class Tetkik(models.Model):
    laboratuvar = models.ForeignKey(Laboratuvar)
    sonuc = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return '{}-{}'.format(self.laboratuvar, self.sonuc)


class LaboratuvarIstek(models.Model):
    hasta = models.ForeignKey(Hasta)
    muayene = models.ForeignKey(Muayene)
    tarih = models.DateField(default=timezone.now, editable=False)
    tetkikler = models.ManyToManyField(Tetkik)

    def __str__(self):
        return '{}-{}-{}'.format(self.pk, self.hasta, self.tarih)


class MuayeneRelatedFile(models.Model):
    hasta = models.ForeignKey(Hasta)
    muayene = models.ForeignKey(Muayene)
    dosya = models.FileField(upload_to='uploads/%Y/%m/%d/')
    yaratim_tarihi = models.DateField(default=timezone.now, editable=False)

    def __str__(self):
        return '{}-{}-{}'.format(self.pk, self.hasta, self.yaratim_tarihi)


class MuayeneAlias(models.Model):
    shorthand = models.CharField(max_length=30)
    longhand = models.CharField(max_length=100)

    def __str__(self):
        return '{}: {}'.format(self.shorthand, self.longhand)
