# -*- coding: utf-8 -*-

import datetime
import itertools

from django.core.urlresolvers import reverse
from django.utils import timezone
from django.utils.text import slugify
from django.db import models


def add_years(date, years):
    try:
        return date.replace(year=date.year + years)
    except ValueError:
        return date + (datetime.date(date.year + years, 1, 1) - datetime.date(date.year, 1, 1))


class Hasta(models.Model):
    CINSIYET = (
        (' ', ' '),
        ('K', 'Kadın'),
        ('E', 'Erkek')
    )

    kayit_tarihi = models.DateField(default=timezone.now, editable=False)
    slug = models.SlugField(max_length=50, editable=False, unique=True)
    ad = models.CharField(max_length=30, blank=False)
    soyad = models.CharField(max_length=30, blank=False)
    tc_kimlik_no = models.CharField(max_length=11, default=' ', blank=True, null=True)
    cinsiyet = models.CharField(max_length=5, blank=True, choices=CINSIYET)
    dogum_tarihi = models.DateField(blank=False)
    meslek = models.CharField(max_length=30, default=' ', blank=True)
    es_ad = models.CharField(max_length=30, default=' ', blank=True)
    es_meslek = models.CharField(max_length=30, default=' ', blank=True)
    cep_telefon = models.CharField(max_length=13, default=' ', blank=True)
    ev_telefon = models.CharField(max_length=13, default=' ', blank=True)
    is_telefon = models.CharField(max_length=13, default=' ', blank=True)
    adres = models.CharField(max_length=255, default=' ', blank=True)
    semt = models.CharField(max_length=30, default=' ', blank=True)
    eposta = models.EmailField(max_length=254, default=' ', blank=True)
    sigorta = models.CharField(max_length=30, default='', blank=True)
    cocuklar = models.CharField(max_length=30, default=' ', blank=True)
    soygecmis = models.CharField(max_length=255, default=' ', blank=True)
    ozgecmis = models.CharField(max_length=255, default=' ', blank=True)
    sigara = models.CharField(max_length=30, default=' ', blank=True)
    alkol = models.CharField(max_length=30, default=' ', blank=True)
    kilo = models.IntegerField(default=None, blank=True, null=True)
    boy = models.IntegerField(default=None, blank=True, null=True)
    legacy_epikriz = models.CharField(max_length=20000, default=' ', blank=True, null=True)
    legacy_ozel_notlar = models.CharField(max_length=1000, default=' ', blank=True, null=True)
    ahsevk_done = models.BooleanField(default=False, verbose_name='AH Sevk Yapıldı')
    ahsevk_done_tarih = models.DateField(blank=True, null=True, default=timezone.now, editable=False, verbose_name='AH Sevk Tarihi')

    class Meta:
        verbose_name = "Hasta"
        verbose_name_plural = "Hastalar"

    def __str__(self):
        hasta = self.ad + " " + self.soyad
        return hasta

    def get_absolute_url(self):
        return reverse('hasta:detail', kwargs={'slug': self.slug})

    def save(self, **kwargs):
        self.slug = orig = slugify(self.ad + " " + self.soyad)

        for x in itertools.count(1):
            if not Hasta.objects.filter(slug=self.slug).exists():
                break
            self.slug = '%s-%d' % (orig, x)

        self.ad = self.ad.upper()
        self.soyad = self.soyad.upper()

        return super().save()

    def age(self):
        today = datetime.date.today()
        born = self.dogum_tarihi
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

    def vki(self):

        try:
            int(self.boy)
            boy = int(self.boy) / 100
        except ValueError:
            return 0

        try:
            kilo = int(self.kilo)
        except ValueError:
            return 0

        try:
            vki = kilo / (boy * boy)
        except ZeroDivisionError:
            return 0

        return float("{0:.2f}".format(vki))

    def get_cocuklar(self):
        cocuklar = "".join(self.cocuklar)
        return cocuklar

    def son_muayene_tarihi(self):
        try:
            return self.muayene_set.last().tarih
        except AttributeError:
            return 'Yok'


class Sozlesme(models.Model):
    hasta = models.ForeignKey('hasta.Hasta', on_delete=models.CASCADE)
    baslangic_tarihi = models.DateField(default=timezone.now, blank=False)
    is_active = models.BooleanField(default=False)

    class Meta:
        get_latest_by = "baslangic_tarihi"
        verbose_name = "Sözleşme"
        verbose_name_plural = "Sözleşmeler"

    def __str__(self):
        hasta = str(self.hasta)
        bitis = str(self.bitis_tarihi())
        baslangic = str(self.baslangic_tarihi)
        return str(hasta + " - " + baslangic + " - " + bitis)

    def bitis_tarihi(self):
        return add_years(self.baslangic_tarihi, 1)

    def get_absolute_url(self):
        return reverse('hasta:sözlesme-detail', kwargs={'slug': self.slug})

    def check_active(self):
        sozlesme_bitis = add_years(self.baslangic_tarihi, 1)
        today = datetime.date.today()
        self.is_active = True if sozlesme_bitis > today else False
        return super(Sozlesme, self).save()

    def days_left(self):
        sozlesme_bitis = self.bitis_tarihi()
        today = datetime.date.today()
        days_left = (sozlesme_bitis - today).days
        return days_left if days_left > 0 else 0
