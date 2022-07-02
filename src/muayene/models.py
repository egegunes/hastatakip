# -*- coding: utf-8 -*-

import datetime

from django.urls import reverse
from django.db import models
from django.utils import timezone


class Ilac(models.Model):
    ad = models.CharField(max_length=30, blank=False, null=False)
    bilgi = models.CharField(max_length=30, blank=True, null=True)
    kullanim = models.CharField(max_length=30, null=True, blank=True)

    class Meta:
        verbose_name = "İlaç"
        verbose_name_plural = "İlaçlar"

    def __str__(self):
        return self.ad

    def get_absolute_url(self):
        return reverse("muayene:ilac-list")


class Recete(models.Model):
    hasta = models.ForeignKey("hasta.Hasta", on_delete=models.CASCADE)
    muayene = models.ForeignKey(
        "muayene.Muayene",
        on_delete=models.CASCADE,
    )
    tarih = models.DateField(default=timezone.now, editable=False)
    ilac1 = models.ForeignKey(
        "muayene.Ilac",
        related_name="ilac1",
        on_delete=models.CASCADE,
        default=1,
        null=False,
        blank=False,
    )
    ilac1_kullanim = models.CharField(
        max_length=100,
        default="Günde 1",
        null=False,
        blank=False,
    )
    ilac1_kutu = models.IntegerField(
        default=1,
        null=False,
        blank=False,
    )
    ilac2 = models.ForeignKey(
        "muayene.Ilac",
        related_name="ilac2",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    ilac2_kullanim = models.CharField(
        max_length=100,
        default=" ",
        null=True,
        blank=True,
    )
    ilac2_kutu = models.IntegerField(
        default=1,
        null=True,
        blank=True,
    )
    ilac3 = models.ForeignKey(
        "muayene.Ilac",
        related_name="ilac3",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    ilac3_kullanim = models.CharField(
        max_length=100,
        default=" ",
        null=True,
        blank=True,
    )
    ilac3_kutu = models.IntegerField(
        default=1,
        null=True,
        blank=True,
    )
    ilac4 = models.ForeignKey(
        "muayene.Ilac",
        related_name="ilac4",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    ilac4_kullanim = models.CharField(
        max_length=100,
        default=" ",
        null=True,
        blank=True,
    )
    ilac4_kutu = models.IntegerField(
        default=1,
        null=True,
        blank=True,
    )
    ilac5 = models.ForeignKey(
        "muayene.Ilac",
        related_name="ilac5",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    ilac5_kullanim = models.CharField(
        max_length=100,
        default=" ",
        null=True,
        blank=True,
    )
    ilac5_kutu = models.IntegerField(
        default=1,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "Reçete"
        verbose_name_plural = "Reçeteler"

    def __str__(self):
        return str(self.tarih)

    def get_absolute_url(self):
        return reverse("muayene:recete-detail", kwargs={"pk": self.pk})


class Rapor(models.Model):
    hasta = models.ForeignKey("hasta.Hasta", on_delete=models.CASCADE)
    muayene = models.ForeignKey("muayene.Muayene", on_delete=models.CASCADE)
    tarih = models.DateField(default=timezone.now, editable=False)
    tani = models.CharField(blank=False, null=False, default=" ", max_length=255)
    gun = models.PositiveSmallIntegerField(
        default=1,
        blank=False,
        null=False,
    )

    class Meta:
        verbose_name = "Rapor"
        verbose_name_plural = "Raporlar"

    def __str__(self):
        return str(self.hasta)

    def get_absolute_url(self):
        return reverse("muayene:rapor-detail", kwargs={"pk": self.pk})


class Laboratuvar(models.Model):
    ad = models.CharField(max_length=30)

    def __str__(self):
        return self.ad


class LaboratuvarIstek(models.Model):
    hasta = models.ForeignKey("hasta.Hasta", on_delete=models.CASCADE)
    muayene = models.ForeignKey(
        "muayene.Muayene",
        on_delete=models.CASCADE,
    )
    tarih = models.DateField(default=timezone.now, editable=False)
    hemogram = models.BooleanField(default=False, verbose_name="Hemogram")
    hemogram_sonuc = models.CharField(
        blank=True, null=True, max_length=100, default=" "
    )
    sedim = models.BooleanField(default=False, verbose_name="Sedim")
    sedim_sonuc = models.CharField(blank=True, null=True, max_length=100, default=" ")
    serum_demir = models.BooleanField(default=False, verbose_name="Serum Demir")
    serum_demir_sonuc = models.CharField(
        blank=True, null=True, max_length=100, default=" "
    )
    tdbk = models.BooleanField(default=False, verbose_name="TDBK")
    tdbk_sonuc = models.CharField(blank=True, null=True, max_length=100, default=" ")
    ferritin = models.BooleanField(default=False, verbose_name="Ferritin")
    ferritin_sonuc = models.CharField(
        blank=True, null=True, max_length=100, default=" "
    )
    b12 = models.BooleanField(default=False, verbose_name="B-12")
    b12_sonuc = models.CharField(blank=True, null=True, max_length=100, default=" ")
    folik_asit = models.BooleanField(default=False, verbose_name="Folik asit")
    folik_asit_sonuc = models.CharField(
        blank=True, null=True, max_length=100, default=" "
    )
    hemoglobin = models.BooleanField(
        default=False, verbose_name="Hemoglobin Elektroforezi"
    )
    hemoglobin_sonuc = models.CharField(
        blank=True, null=True, max_length=100, default=" "
    )
    aclik_kan = models.BooleanField(default=False, verbose_name="Açlık Kan Şekeri")
    aclik_kan_sonuc = models.CharField(
        blank=True, null=True, max_length=100, default=" "
    )
    tokluk_kan = models.BooleanField(default=False, verbose_name="Tokluk Kan Şekeri")
    tokluk_kan_sonuc = models.CharField(
        blank=True, null=True, max_length=100, default=" "
    )
    hba1c = models.BooleanField(default=False, verbose_name="HbA1c")
    hba1c_sonuc = models.CharField(blank=True, null=True, max_length=100, default=" ")
    sgot = models.BooleanField(default=False, verbose_name="SGOT (AST)")
    sgot_sonuc = models.CharField(blank=True, null=True, max_length=100, default=" ")
    sgpt = models.BooleanField(default=False, verbose_name="SGPT (ALT)")
    sgpt_sonuc = models.CharField(blank=True, null=True, max_length=100, default=" ")
    ggt = models.BooleanField(default=False, verbose_name="GGT")
    ggt_sonuc = models.CharField(blank=True, null=True, max_length=100, default=" ")
    alp = models.BooleanField(default=False, verbose_name="ALP")
    alp_sonuc = models.CharField(blank=True, null=True, max_length=100, default=" ")
    ure = models.BooleanField(default=False, verbose_name="Üre")
    ure_sonuc = models.CharField(blank=True, null=True, max_length=100, default=" ")
    kreatinin = models.BooleanField(default=False, verbose_name="Kreatinin")
    kreatinin_sonuc = models.CharField(
        blank=True, null=True, max_length=100, default=" "
    )
    urik_asit = models.BooleanField(default=False, verbose_name="Ürik asit")
    urik_asit_sonuc = models.CharField(
        blank=True, null=True, max_length=100, default=" "
    )
    total_kolesterol = models.BooleanField(
        default=False, verbose_name="Total Kolesterol"
    )
    total_kolesterol_sonuc = models.CharField(
        blank=True, null=True, max_length=100, default=" "
    )
    hdl = models.BooleanField(default=False, verbose_name="HDL")
    hdl_sonuc = models.CharField(blank=True, null=True, max_length=100, default=" ")
    trigliserit = models.BooleanField(default=False, verbose_name="Trigliserit")
    trigliserit_sonuc = models.CharField(
        blank=True, null=True, max_length=100, default=" "
    )
    ldl = models.BooleanField(default=False, verbose_name="LDL")
    ldl_sonuc = models.CharField(blank=True, null=True, max_length=100, default=" ")
    free_t3 = models.BooleanField(default=False, verbose_name="Free T3")
    free_t3_sonuc = models.CharField(blank=True, null=True, max_length=100, default=" ")
    free_t4 = models.BooleanField(default=False, verbose_name="Free T4")
    free_t4_sonuc = models.CharField(blank=True, null=True, max_length=100, default=" ")
    tsh = models.BooleanField(default=False, verbose_name="TSH")
    tsh_sonuc = models.CharField(blank=True, null=True, max_length=100, default=" ")
    anti_tpo = models.BooleanField(default=False, verbose_name="anti-TPO")
    anti_tpo_sonuc = models.CharField(
        blank=True, null=True, max_length=100, default=" "
    )
    anti_tg = models.BooleanField(default=False, verbose_name="anti-TG")
    anti_tg_sonuc = models.CharField(blank=True, null=True, max_length=100, default=" ")
    aso = models.BooleanField(default=False, verbose_name="ASO")
    aso_sonuc = models.CharField(blank=True, null=True, max_length=100, default=" ")
    crp = models.BooleanField(default=False, verbose_name="CRP")
    crp_sonuc = models.CharField(blank=True, null=True, max_length=100, default=" ")
    rf = models.BooleanField(default=False, verbose_name="RF")
    rf_sonuc = models.CharField(blank=True, null=True, max_length=100, default=" ")
    psa = models.BooleanField(default=False, verbose_name="PSA")
    psa_sonuc = models.CharField(blank=True, null=True, max_length=100, default=" ")
    free_psa = models.BooleanField(default=False, verbose_name="Free PSA")
    free_psa_sonuc = models.CharField(
        blank=True, null=True, max_length=100, default=" "
    )
    tam_idrar = models.BooleanField(default=False, verbose_name="Tam İdrar")
    tam_idrar_sonuc = models.CharField(
        blank=True, null=True, max_length=100, default=" "
    )
    idrar_kab = models.BooleanField(default=False, verbose_name="İdrar KAB")
    idrar_kab_sonuc = models.CharField(
        blank=True, null=True, max_length=100, default=" "
    )
    gaita = models.BooleanField(default=False, verbose_name="Gaita Direkt Bakısı")
    gaita_sonuc = models.CharField(blank=True, null=True, max_length=100, default=" ")
    bogaz_kab = models.BooleanField(default=False, verbose_name="Boğaz KAB")
    bogaz_kab_sonuc = models.CharField(
        blank=True, null=True, max_length=100, default=" "
    )
    ejaculat_kab = models.BooleanField(default=False, verbose_name="Ejaculat KAB")
    ejaculat_kab_sonuc = models.CharField(
        blank=True, null=True, max_length=100, default=" "
    )
    ekg = models.BooleanField(default=False, verbose_name="EKG")
    ekg_sonuc = models.CharField(blank=True, null=True, max_length=100, default=" ")
    eforlu_ekg = models.BooleanField(default=False, verbose_name="Eforlu EKG")
    eforlu_ekg_sonuc = models.CharField(
        blank=True, null=True, max_length=100, default=" "
    )
    ekokardiografi = models.BooleanField(default=False, verbose_name="Ekokardiografi")
    ekokardiografi_sonuc = models.CharField(
        blank=True, null=True, max_length=100, default=" "
    )
    tansiyon_holter = models.BooleanField(default=False, verbose_name="Tansiyon Holter")
    tansiyon_holter_sonuc = models.CharField(
        blank=True, null=True, max_length=100, default=" "
    )
    ekg_holter = models.BooleanField(default=False, verbose_name="EKG Holter")
    ekg_holter_sonuc = models.CharField(
        blank=True, null=True, max_length=100, default=" "
    )
    pa_akciger = models.BooleanField(default=False, verbose_name="PA Akciğer Grafisi")
    pa_akciger_sonuc = models.CharField(
        blank=True, null=True, max_length=100, default=" "
    )
    waters = models.BooleanField(default=False, verbose_name="Waters Grafisi")
    waters_sonuc = models.CharField(blank=True, null=True, max_length=100, default=" ")
    ikiyonlu_servikal = models.BooleanField(
        default=False, verbose_name="2 Yönlü Servikal Grafisi"
    )
    ikiyonlu_servikal_sonuc = models.CharField(
        blank=True, null=True, max_length=100, default=" "
    )
    ikiyonlu_lsv = models.BooleanField(
        default=False, verbose_name="2 Yönlü LSV Grafisi"
    )
    ikiyonlu_lsv_sonuc = models.CharField(
        blank=True, null=True, max_length=100, default=" "
    )
    tum_batin = models.BooleanField(default=False, verbose_name="Tüm Batın US")
    tum_batin_sonuc = models.CharField(
        blank=True, null=True, max_length=100, default=" "
    )
    ust_batin = models.BooleanField(default=False, verbose_name="Üst Batın US")
    ust_batin_sonuc = models.CharField(
        blank=True, null=True, max_length=100, default=" "
    )
    alt_batin = models.BooleanField(default=False, verbose_name="Alt Batın US")
    alt_batin_sonuc = models.CharField(
        blank=True, null=True, max_length=100, default=" "
    )
    uriner = models.BooleanField(default=False, verbose_name="Üriner US")
    uriner_sonuc = models.CharField(blank=True, null=True, max_length=100, default=" ")
    tiroid = models.BooleanField(default=False, verbose_name="Tiroid US")
    tiroid_sonuc = models.CharField(blank=True, null=True, max_length=100, default=" ")
    meme = models.BooleanField(default=False, verbose_name="Meme US")
    meme_sonuc = models.CharField(blank=True, null=True, max_length=100, default=" ")
    tiroid_sintigrafi = models.BooleanField(
        default=False, verbose_name="Tiroid Sintigrafisi"
    )
    tiroid_sintigrafi_sonuc = models.CharField(
        blank=True, null=True, max_length=100, default=" "
    )
    aclik_insulin = models.BooleanField(default=False, verbose_name="Açlık İnsülin")
    aclik_insulin_sonuc = models.CharField(
        blank=True, null=True, max_length=100, default=" "
    )
    yuzyirmi_insulin = models.BooleanField(default=False, verbose_name="120 dk İnsülin")
    yuzyirmi_insulin_sonuc = models.CharField(
        blank=True, null=True, max_length=100, default=" "
    )
    yirmibesohd = models.BooleanField(default=False, verbose_name="25 OH D3")
    yirmibesohd_sonuc = models.CharField(
        blank=True, null=True, max_length=100, default=" "
    )
    og11 = models.BooleanField(
        default=False, verbose_name="OGTT (75 gr Glikoz ile 0-60-120-180 dakikalarda)"
    )
    og11_sonuc = models.CharField(blank=True, null=True, max_length=100, default=" ")
    custom1_ad = models.CharField(
        blank=True,
        null=True,
        max_length=30,
        default="",
    )
    custom1 = models.BooleanField(default=False)
    custom1_sonuc = models.CharField(blank=True, null=True, max_length=100, default="")
    custom2_ad = models.CharField(
        blank=True,
        null=True,
        max_length=30,
        default="",
    )
    custom2 = models.BooleanField(default=False)
    custom2_sonuc = models.CharField(blank=True, null=True, max_length=100, default="")
    custom3_ad = models.CharField(
        blank=True,
        null=True,
        max_length=30,
        default="",
    )
    custom3 = models.BooleanField(default=False)
    custom3_sonuc = models.CharField(blank=True, null=True, max_length=100, default="")
    custom4_ad = models.CharField(
        blank=True,
        null=True,
        max_length=30,
        default="",
    )
    custom4 = models.BooleanField(default=False)
    custom4_sonuc = models.CharField(blank=True, null=True, max_length=100, default="")
    custom5_ad = models.CharField(
        blank=True,
        null=True,
        max_length=30,
        default="",
    )
    custom5 = models.BooleanField(default=False)
    custom5_sonuc = models.CharField(blank=True, null=True, max_length=100, default="")

    class Meta:
        verbose_name = "Laboratuvar Istek"
        verbose_name_plural = "Laboratuvar Istekleri"

    def __str__(self):
        return str(self.hasta)

    def get_absolute_url(self):
        return reverse("muayene:lab-detail", kwargs={"pk": self.pk})

    def get_true_fields(self):
        true_fields = []
        for field in LaboratuvarIstek._meta.fields:
            value = field.value_to_string(self)
            if value == "True":
                if field == LaboratuvarIstek._meta.get_field("custom1"):
                    true_fields.append(self.custom1_ad)
                elif field == LaboratuvarIstek._meta.get_field("custom2"):
                    true_fields.append(self.custom2_ad)
                elif field == LaboratuvarIstek._meta.get_field("custom3"):
                    true_fields.append(self.custom3_ad)
                elif field == LaboratuvarIstek._meta.get_field("custom4"):
                    true_fields.append(self.custom4_ad)
                elif field == LaboratuvarIstek._meta.get_field("custom5"):
                    true_fields.append(self.custom5_ad)
                else:
                    true_fields.append(field.verbose_name)

        return true_fields


class MuayeneRelatedFile(models.Model):
    hasta = models.ForeignKey("hasta.Hasta", on_delete=models.CASCADE)
    muayene = models.ForeignKey(
        "muayene.Muayene",
        on_delete=models.CASCADE,
    )
    dosya = models.FileField(upload_to="uploads/%Y/%m/%d/")
    yaratim_tarihi = models.DateField(default=timezone.now, editable=False)

    def __str__(self):
        hasta = self.hasta.ad + self.hasta.soyad
        return hasta


class Muayene(models.Model):
    hasta = models.ForeignKey("hasta.Hasta", on_delete=models.CASCADE)
    tarih = models.DateField(default=timezone.now, editable=False)
    yakinma = models.TextField(
        max_length=255,
        default=" ",
        blank=True,
    )
    kullandigi_ilaclar = models.TextField(max_length=512, default=" ", blank=True)
    baki = models.TextField(
        max_length=255,
        default=" ",
        blank=True,
    )
    ontani_tani = models.TextField(
        max_length=255,
        default=" ",
        blank=True,
    )
    oneri_gorusler = models.TextField(
        max_length=255,
        default=" ",
        blank=True,
    )
    ozel_notlar = models.TextField(
        max_length=255,
        default=" ",
        blank=True,
    )

    class Meta:
        get_latest_by = "tarih"
        verbose_name = "Muayene"
        verbose_name_plural = "Muayeneler"

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("muayene:detail", kwargs={"pk": self.pk})

    def was_today(self):
        today = datetime.date.today()
        return True if self.tarih == today else False


class MuayeneAlias(models.Model):
    shorthand = models.CharField(blank=False, null=False, max_length=30)
    longhand = models.CharField(blank=False, null=False, max_length=100)

    def __str__(self):
        alias = self.shorthand + ": " + self.longhand
        return str(alias)

    def get_absolute_url(self):
        return reverse("muayene:alias-list")
