# -*- coding: utf-8 -*-

import datetime

from django.utils.translation import ugettext_lazy as _
from django import forms

from dal import autocomplete

from hasta.models import Hasta
from muayene.models import (
    Muayene,
    Ilac,
    Recete,
    Rapor,
    LaboratuvarIstek,
    Laboratuvar,
    MuayeneRelatedFile,
    MuayeneAlias,
)


class MuayeneCreateForm(forms.ModelForm):
    hasta = forms.ModelChoiceField(
        required=True,
        queryset=Hasta.objects.all(),
        widget=autocomplete.ModelSelect2(url="hastaAutocomplete"),
        label=_("Hasta"),
    )
    yakinma = forms.CharField(
        max_length=255,
        required=False,
        widget=forms.widgets.TextInput(attrs={"class": "form-control"}),
        label=_("Yakınma"),
    )
    kullandigi_ilaclar = forms.CharField(
        max_length=255,
        required=False,
        widget=forms.widgets.TextInput(attrs={"class": "form-control"}),
        label=_("Kullandığı ilaçlar"),
    )
    baki = forms.CharField(
        max_length=255,
        required=False,
        widget=forms.widgets.TextInput(attrs={"class": "form-control"}),
        label=_("Fizik bakı"),
    )
    ontani_tani = forms.CharField(
        max_length=255,
        required=False,
        widget=forms.widgets.TextInput(attrs={"class": "form-control"}),
        label=_("Öntanı / tanı"),
    )
    oneri_gorusler = forms.CharField(
        max_length=255,
        required=False,
        widget=forms.widgets.TextInput(attrs={"class": "form-control"}),
        label=_("Öneri ve görüşler"),
    )
    ozel_notlar = forms.CharField(
        max_length=255,
        required=False,
        widget=forms.widgets.TextInput(attrs={"class": "form-control"}),
        label=_("Özel notlar"),
    )

    class Meta:
        model = Muayene
        fields = "__all__"


class IlacCreateForm(forms.ModelForm):
    ad = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.widgets.TextInput(attrs={"class": "form-control"}),
        label=_("Ad"),
    )
    kullanim = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.widgets.TextInput(attrs={"class": "form-control"}),
        label=_("Kullanım"),
    )
    bilgi = forms.CharField(
        max_length=30,
        required=False,
        widget=forms.widgets.TextInput(attrs={"class": "form-control"}),
        label=_("Bilgi"),
    )

    class Meta:
        model = Ilac
        fields = "__all__"


class ReceteCreateForm(forms.Form):
    kutu_sayisi = (
        (1, "1 kutu"),
        (2, "2 kutu"),
        (3, "3 kutu"),
        (4, "4 kutu"),
        (5, "5 kutu"),
        (6, "6 kutu"),
        (7, "7 kutu"),
        (8, "8 kutu"),
        (9, "9 kutu"),
        (10, "10 kutu"),
    )
    ilac1 = forms.ModelChoiceField(
        required=True,
        queryset=Ilac.objects.all(),
        widget=autocomplete.ModelSelect2(
            url="IlacAutocomplete", attrs={"class": "ilac_select2"}
        ),
    )
    ilac1_kullanim = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.widgets.TextInput(
            attrs={"class": "form-control ilac_kullanim", "placeholder": "Kullanım"}
        ),
    )
    ilac1_kutu = forms.ChoiceField(
        required=True,
        widget=forms.widgets.Select(attrs={"class": "form-control"}),
        choices=kutu_sayisi,
    )
    ilac2 = forms.ModelChoiceField(
        required=False,
        queryset=Ilac.objects.all(),
        widget=autocomplete.ModelSelect2(
            url="IlacAutocomplete", attrs={"class": "ilac_select2"}
        ),
    )
    ilac2_kullanim = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.widgets.TextInput(
            attrs={"class": "form-control ilac_kullanim", "placeholder": "Kullanım"}
        ),
    )
    ilac2_kutu = forms.ChoiceField(
        required=False,
        widget=forms.widgets.Select(attrs={"class": "form-control"}),
        choices=kutu_sayisi,
    )
    ilac3 = forms.ModelChoiceField(
        required=False,
        queryset=Ilac.objects.all(),
        widget=autocomplete.ModelSelect2(
            url="IlacAutocomplete", attrs={"class": "ilac_select2"}
        ),
    )
    ilac3_kullanim = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.widgets.TextInput(
            attrs={"class": "form-control ilac_kullanim", "placeholder": "Kullanım"}
        ),
    )
    ilac3_kutu = forms.ChoiceField(
        required=False,
        widget=forms.widgets.Select(attrs={"class": "form-control"}),
        choices=kutu_sayisi,
    )
    ilac4 = forms.ModelChoiceField(
        required=False,
        queryset=Ilac.objects.all(),
        widget=autocomplete.ModelSelect2(
            url="IlacAutocomplete", attrs={"class": "ilac_select2"}
        ),
    )
    ilac4_kullanim = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.widgets.TextInput(
            attrs={"class": "form-control ilac_kullanim", "placeholder": "Kullanım"}
        ),
    )
    ilac4_kutu = forms.ChoiceField(
        required=False,
        widget=forms.widgets.Select(attrs={"class": "form-control"}),
        choices=kutu_sayisi,
    )
    ilac5 = forms.ModelChoiceField(
        required=False,
        queryset=Ilac.objects.all(),
        widget=autocomplete.ModelSelect2(
            url="IlacAutocomplete", attrs={"class": "ilac_select2"}
        ),
    )
    ilac5_kullanim = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.widgets.TextInput(
            attrs={"class": "form-control ilac_kullanim", "placeholder": "Kullanım"}
        ),
    )
    ilac5_kutu = forms.ChoiceField(
        required=False,
        widget=forms.widgets.Select(attrs={"class": "form-control"}),
        choices=kutu_sayisi,
    )


class RaporCreateForm(forms.Form):
    tani = forms.CharField(
        max_length=255,
        required=True,
        widget=forms.widgets.TextInput(attrs={"class": "form-control"}),
        label=_("Tanı"),
    )
    gun = forms.IntegerField(
        required=True,
        widget=forms.widgets.NumberInput(attrs={"class": "form-control"}),
        label=_("Gün"),
    )


class LaboratuvarIstekForm(forms.Form):
    hemogram = forms.BooleanField(
        required=False,
    )
    hemogram_sonuc = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.widgets.TextInput(attrs={"class": "form-control"}),
    )
    sedim = forms.BooleanField(
        required=False,
    )
    sedim_sonuc = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.widgets.TextInput(attrs={"class": "form-control"}),
    )
    serum_demir = forms.BooleanField(
        required=False,
    )
    serum_demir_sonuc = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.widgets.TextInput(attrs={"class": "form-control"}),
    )
    tdbk = forms.BooleanField(
        required=False,
    )
    tdbk_sonuc = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.widgets.TextInput(attrs={"class": "form-control"}),
    )
    ferritin = forms.BooleanField(
        required=False,
    )
    ferritin_sonuc = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.widgets.TextInput(attrs={"class": "form-control"}),
    )
    b12 = forms.BooleanField(
        required=False,
    )
    b12_sonuc = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.widgets.TextInput(attrs={"class": "form-control"}),
    )
    folik_asit = forms.BooleanField(
        required=False,
    )
    folik_asit_sonuc = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.widgets.TextInput(attrs={"class": "form-control"}),
    )
    hemoglobin = forms.BooleanField(
        required=False,
    )
    hemoglobin_sonuc = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.widgets.TextInput(attrs={"class": "form-control"}),
    )
    aclik_kan = forms.BooleanField(
        required=False,
    )
    aclik_kan_sonuc = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.widgets.TextInput(attrs={"class": "form-control"}),
    )
    tokluk_kan = forms.BooleanField(
        required=False,
    )
    tokluk_kan_sonuc = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.widgets.TextInput(attrs={"class": "form-control"}),
    )
    hba1c = forms.BooleanField(
        required=False,
    )
    hba1c_sonuc = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.widgets.TextInput(attrs={"class": "form-control"}),
    )
    sgot = forms.BooleanField(
        required=False,
    )
    sgot_sonuc = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.widgets.TextInput(attrs={"class": "form-control"}),
    )
    sgpt = forms.BooleanField(
        required=False,
    )
    sgpt_sonuc = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.widgets.TextInput(attrs={"class": "form-control"}),
    )
    ggt = forms.BooleanField(
        required=False,
    )
    ggt_sonuc = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.widgets.TextInput(attrs={"class": "form-control"}),
    )
    alp = forms.BooleanField(
        required=False,
    )
    alp_sonuc = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.widgets.TextInput(attrs={"class": "form-control"}),
    )
    ure = forms.BooleanField(
        required=False,
    )
    ure_sonuc = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.widgets.TextInput(attrs={"class": "form-control"}),
    )
    kreatinin = forms.BooleanField(
        required=False,
    )
    kreatinin_sonuc = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.widgets.TextInput(attrs={"class": "form-control"}),
    )
    urik_asit = forms.BooleanField(
        required=False,
    )
    urik_asit_sonuc = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.widgets.TextInput(attrs={"class": "form-control"}),
    )
    total_kolesterol = forms.BooleanField(
        required=False,
    )
    total_kolesterol_sonuc = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.widgets.TextInput(attrs={"class": "form-control"}),
    )
    hdl = forms.BooleanField(
        required=False,
    )
    hdl_sonuc = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.widgets.TextInput(attrs={"class": "form-control"}),
    )
    trigliserit = forms.BooleanField(
        required=False,
    )
    trigliserit_sonuc = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.widgets.TextInput(attrs={"class": "form-control"}),
    )
    ldl = forms.BooleanField(
        required=False,
    )
    ldl_sonuc = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.widgets.TextInput(attrs={"class": "form-control"}),
    )
    free_t3 = forms.BooleanField(
        required=False,
    )
    free_t3_sonuc = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.widgets.TextInput(attrs={"class": "form-control"}),
    )
    free_t4 = forms.BooleanField(
        required=False,
    )
    free_t4_sonuc = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.widgets.TextInput(attrs={"class": "form-control"}),
    )
    tsh = forms.BooleanField(
        required=False,
    )
    tsh_sonuc = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.widgets.TextInput(attrs={"class": "form-control"}),
    )
    anti_tpo = forms.BooleanField(
        required=False,
    )
    anti_tpo_sonuc = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.widgets.TextInput(attrs={"class": "form-control"}),
    )
    anti_tg = forms.BooleanField(
        required=False,
    )
    anti_tg_sonuc = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.widgets.TextInput(attrs={"class": "form-control"}),
    )
    aso = forms.BooleanField(
        required=False,
    )
    aso_sonuc = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.widgets.TextInput(attrs={"class": "form-control"}),
    )
    crp = forms.BooleanField(
        required=False,
    )
    crp_sonuc = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.widgets.TextInput(attrs={"class": "form-control"}),
    )
    rf = forms.BooleanField(
        required=False,
    )
    rf_sonuc = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.widgets.TextInput(attrs={"class": "form-control"}),
    )
    psa = forms.BooleanField(
        required=False,
    )
    psa_sonuc = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.widgets.TextInput(attrs={"class": "form-control"}),
    )
    free_psa = forms.BooleanField(
        required=False,
    )
    free_psa_sonuc = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.widgets.TextInput(attrs={"class": "form-control"}),
    )
    tam_idrar = forms.BooleanField(
        required=False,
    )
    tam_idrar_sonuc = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.widgets.TextInput(attrs={"class": "form-control"}),
    )
    idrar_kab = forms.BooleanField(
        required=False,
    )
    idrar_kab_sonuc = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.widgets.TextInput(attrs={"class": "form-control"}),
    )
    gaita = forms.BooleanField(
        required=False,
    )
    gaita_sonuc = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.widgets.TextInput(attrs={"class": "form-control"}),
    )
    bogaz_kab = forms.BooleanField(
        required=False,
    )
    bogaz_kab_sonuc = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.widgets.TextInput(attrs={"class": "form-control"}),
    )
    ejaculat_kab = forms.BooleanField(
        required=False,
    )
    ejaculat_kab_sonuc = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.widgets.TextInput(attrs={"class": "form-control"}),
    )
    ekg = forms.BooleanField(
        required=False,
    )
    ekg_sonuc = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.widgets.TextInput(attrs={"class": "form-control"}),
    )
    eforlu_ekg = forms.BooleanField(
        required=False,
    )
    eforlu_ekg_sonuc = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.widgets.TextInput(attrs={"class": "form-control"}),
    )
    ekokardiografi = forms.BooleanField(
        required=False,
    )
    ekokardiografi_sonuc = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.widgets.TextInput(attrs={"class": "form-control"}),
    )
    tansiyon_holter = forms.BooleanField(
        required=False,
    )
    tansiyon_holter_sonuc = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.widgets.TextInput(attrs={"class": "form-control"}),
    )
    ekg_holter = forms.BooleanField(
        required=False,
    )
    ekg_holter_sonuc = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.widgets.TextInput(attrs={"class": "form-control"}),
    )
    pa_akciger = forms.BooleanField(
        required=False,
    )
    pa_akciger_sonuc = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.widgets.TextInput(attrs={"class": "form-control"}),
    )
    waters = forms.BooleanField(
        required=False,
    )
    waters_sonuc = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.widgets.TextInput(attrs={"class": "form-control"}),
    )
    ikiyonlu_servikal = forms.BooleanField(
        required=False,
    )
    ikiyonlu_servikal_sonuc = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.widgets.TextInput(attrs={"class": "form-control"}),
    )
    ikiyonlu_lsv = forms.BooleanField(
        required=False,
    )
    ikiyonlu_lsv_sonuc = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.widgets.TextInput(attrs={"class": "form-control"}),
    )
    tum_batin = forms.BooleanField(
        required=False,
    )
    tum_batin_sonuc = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.widgets.TextInput(attrs={"class": "form-control"}),
    )
    ust_batin = forms.BooleanField(
        required=False,
    )
    ust_batin_sonuc = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.widgets.TextInput(attrs={"class": "form-control"}),
    )
    alt_batin = forms.BooleanField(
        required=False,
    )
    alt_batin_sonuc = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.widgets.TextInput(attrs={"class": "form-control"}),
    )
    uriner = forms.BooleanField(
        required=False,
    )
    uriner_sonuc = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.widgets.TextInput(attrs={"class": "form-control"}),
    )
    tiroid = forms.BooleanField(
        required=False,
    )
    tiroid_sonuc = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.widgets.TextInput(attrs={"class": "form-control"}),
    )
    meme = forms.BooleanField(
        required=False,
    )
    meme_sonuc = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.widgets.TextInput(attrs={"class": "form-control"}),
    )
    tiroid_sintigrafi = forms.BooleanField(
        required=False,
    )
    tiroid_sintigrafi_sonuc = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.widgets.TextInput(attrs={"class": "form-control"}),
    )
    aclik_insulin = forms.BooleanField(
        required=False,
    )
    aclik_insulin_sonuc = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.widgets.TextInput(attrs={"class": "form-control"}),
    )
    yuzyirmi_insulin = forms.BooleanField(
        required=False,
    )
    yuzyirmi_insulin_sonuc = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.widgets.TextInput(attrs={"class": "form-control"}),
    )
    yirmibesohd = forms.BooleanField(
        required=False,
    )
    yirmibesohd_sonuc = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.widgets.TextInput(attrs={"class": "form-control"}),
    )
    og11 = forms.BooleanField(
        required=False,
    )
    og11_sonuc = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.widgets.TextInput(attrs={"class": "form-control"}),
    )
    custom1_ad = forms.CharField(
        max_length=30,
        required=False,
        widget=forms.widgets.TextInput(attrs={"class": "form-control"}),
    )
    custom1 = forms.BooleanField(required=False)
    custom1_sonuc = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.widgets.TextInput(attrs={"class": "form-control"}),
    )
    custom2_ad = forms.CharField(
        max_length=30,
        required=False,
        widget=forms.widgets.TextInput(attrs={"class": "form-control"}),
    )
    custom2 = forms.BooleanField(required=False)
    custom2_sonuc = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.widgets.TextInput(attrs={"class": "form-control"}),
    )
    custom3_ad = forms.CharField(
        max_length=30,
        required=False,
        widget=forms.widgets.TextInput(attrs={"class": "form-control"}),
    )
    custom3 = forms.BooleanField(required=False)
    custom3_sonuc = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.widgets.TextInput(attrs={"class": "form-control"}),
    )
    custom4_ad = forms.CharField(
        max_length=30,
        required=False,
        widget=forms.widgets.TextInput(attrs={"class": "form-control"}),
    )
    custom4 = forms.BooleanField(required=False)
    custom4_sonuc = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.widgets.TextInput(attrs={"class": "form-control"}),
    )
    custom5_ad = forms.CharField(
        max_length=30,
        required=False,
        widget=forms.widgets.TextInput(attrs={"class": "form-control"}),
    )
    custom5 = forms.BooleanField(required=False)
    custom5_sonuc = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.widgets.TextInput(attrs={"class": "form-control"}),
    )


class DateRangeForm(forms.Form):
    DATE_CHOICES = (("Hafta", "Bu hafta"), ("Ay", "Bu ay"), ("Yıl", "Bu yıl"))
    start_date = forms.DateField(
        widget=forms.widgets.DateInput(
            attrs={
                "class": "form-control datepicker input-sm",
                "name": "start",
                "placeholder": "Başlangıç tarihi",
            }
        ),
        required=True,
    )
    end_date = forms.DateField(
        widget=forms.widgets.DateInput(
            attrs={
                "class": "form-control datepicker input-sm",
                "name": "end",
                "placeholder": "Bitiş tarihi",
            }
        ),
        required=True,
    )


class MuayeneRelatedFileForm(forms.Form):
    dosya = forms.FileField(
        required=True,
        widget=forms.widgets.FileInput(attrs={"class": "form-control"}),
        label=_("Dosya"),
    )


class MuayeneAliasCreateForm(forms.ModelForm):
    shorthand = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.widgets.TextInput(attrs={"class": "form-control"}),
    )
    longhand = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.widgets.TextInput(attrs={"class": "form-control"}),
    )

    class Meta:
        model = MuayeneAlias
        fields = "__all__"
