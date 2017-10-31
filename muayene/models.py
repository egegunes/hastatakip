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
        verbose_name = "Muayene"
        verbose_name_plural = "Muayeneler"

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

    class Meta:
        verbose_name = "İlaç"
        verbose_name_plural = "İlaçlar"

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

    class Meta:
        verbose_name = "Reçete"
        verbose_name_plural = "Reçeteler"

    def __str__(self):
        return '{}-{}-{}'.format(self.pk, self.hasta, self.tarih)


class Rapor(models.Model):
    hasta = models.ForeignKey(Hasta)
    muayene = models.ForeignKey(Muayene)
    tarih = models.DateField(default=timezone.now, editable=False)
    tani = models.CharField(max_length=255)
    gun = models.PositiveSmallIntegerField(default=1)

    class Meta:
        verbose_name = "Rapor"
        verbose_name_plural = "Raporlar"

    def __str__(self):
        return '{}-{}-{}'.format(self.pk, self.hasta, self.tarih)


class Laboratuvar(models.Model):
    ad = models.CharField(max_length=30)

    class Meta:
        verbose_name = "Laboratuvar"
        verbose_name_plural = "Laboratuvarlar"

    def __str__(self):
        return '{}'.format(self.ad)


class Tetkik(models.Model):
    laboratuvar = models.ForeignKey(Laboratuvar)
    sonuc = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = "Tetkik"
        verbose_name_plural = "Tetkikler"

    def __str__(self):
        return '{}-{}'.format(self.laboratuvar, self.sonuc)


class LaboratuvarIstek(models.Model):
    hasta = models.ForeignKey(Hasta)
    muayene = models.ForeignKey(Muayene)
    tarih = models.DateField(default=timezone.now, editable=False)
    tetkikler = models.ManyToManyField(Tetkik)

    class Meta:
        verbose_name = "Laboratuvar Istek"
        verbose_name_plural = "Laboratuvar Istekler"

    def __str__(self):
        return '{}-{}-{}'.format(self.pk, self.hasta, self.tarih)


class MuayeneRelatedFile(models.Model):
    hasta = models.ForeignKey(Hasta)
    muayene = models.ForeignKey(Muayene)
    dosya = models.FileField(upload_to='uploads/%Y/%m/%d/')
    yaratim_tarihi = models.DateField(default=timezone.now, editable=False)

    class Meta:
        verbose_name = "Dosya"
        verbose_name_plural = "Dosyalar"

    def __str__(self):
        return '{}-{}-{}'.format(self.pk, self.hasta, self.yaratim_tarihi)


class MuayeneAlias(models.Model):
    shorthand = models.CharField(max_length=30)
    longhand = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Kısaltma"
        verbose_name_plural = "Kısaltmalar"

    def __str__(self):
        return '{}: {}'.format(self.shorthand, self.longhand)
