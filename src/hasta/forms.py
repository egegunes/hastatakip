# -*- coding: utf-8 -*-

from django.utils.translation import ugettext_lazy as _
from django import forms

from hasta.models import Hasta
from hasta.fields import ListTextWidget


class HastaCreateForm(forms.ModelForm):
    SIGORTA = (
        'ALLIANZ',
        'ALLIANZ KURUMSAL',
        'EUROKA',
        'GROUPAMA',
        'MAPPFRE',
        'AKSIGORTA',
        'ACIBADEM',
        'CHECKUP')
    CINSIYET = (
        (' ', ' '),
        ('K', 'Kadın'),
        ('E', 'Erkek')
    )
    ad = forms.CharField(
        required=True,
        max_length=30,
        widget=forms.widgets.TextInput(attrs={'class': 'form-control'}),
        label=_('Ad')
    )
    soyad = forms.CharField(
        required=True,
        max_length=30,
        widget=forms.widgets.TextInput(attrs={'class': 'form-control'}),
        label=_('Soyad')
    )
    tc_kimlik_no = forms.CharField(
        required=False,
        max_length=11,
        widget=forms.widgets.TextInput(attrs={'class': 'form-control'}),
        label=_('TC Kimlik No')
    )
    cinsiyet = forms.ChoiceField(
        required=True,
        widget=forms.widgets.Select(attrs={'class': 'form-control'}),
        choices=CINSIYET,
        label=_('Cinsiyet')
    )
    dogum_tarihi = forms.DateField(
        required=True,
        widget=forms.widgets.DateInput(attrs={'class': 'form-control datepicker'}),
        label=_('Doğum tarihi')
    )
    meslek = forms.CharField(
        required=False,
        max_length=30,
        widget=forms.widgets.TextInput(attrs={'class': 'form-control'}),
        label=_('Meslek')
    )
    es_ad = forms.CharField(
        required=False,
        max_length=30,
        widget=forms.widgets.TextInput(attrs={'class': 'form-control'}),
        label=_('Eş ad')
    )
    es_meslek = forms.CharField(
        required=False,
        max_length=30,
        widget=forms.widgets.TextInput(attrs={'class': 'form-control'}),
        label=_('Eş meslek')
    )
    cep_telefon = forms.CharField(
        required=False,
        max_length=13,
        widget=forms.widgets.TextInput(attrs={'class': 'form-control'}),
        label=_('Cep telefon')
    )
    ev_telefon = forms.CharField(
        required=False,
        max_length=13,
        widget=forms.widgets.TextInput(attrs={'class': 'form-control'}),
        label=_('Ev telefon')
    )
    is_telefon = forms.CharField(
        required=False,
        max_length=13,
        widget=forms.widgets.TextInput(attrs={'class': 'form-control'}),
        label=_('İş telefon')
    )
    adres = forms.CharField(
        required=False,
        max_length=255,
        widget=forms.widgets.TextInput(attrs={'class': 'form-control'}),
        label=_('Adres')
    )
    semt = forms.CharField(
        required=False,
        max_length=30,
        widget=forms.widgets.TextInput(attrs={'class': 'form-control'}),
        label=_('Semt')
    )
    eposta = forms.CharField(
        required=False,
        max_length=254,
        widget=forms.widgets.EmailInput(attrs={'class': 'form-control'}),
        label=_('Eposta Adresi')
    )
    sigorta = forms.CharField(
        required=False,
        widget=ListTextWidget(choices=SIGORTA, name='sigorta_list', attrs={'class': 'form-control'}),
        label=_('Sigorta')
    )
    cocuklar = forms.CharField(
        required=False,
        max_length=30,
        widget=forms.widgets.TextInput(attrs={'class': 'form-control'}),
        label=_('Çocuklar')
    )
    soygecmis = forms.CharField(
        required=False,
        max_length=255,
        widget=forms.widgets.TextInput(attrs={'class': 'form-control'}),
        label=_('Soygeçmiş')
    )
    ozgecmis = forms.CharField(
        required=False,
        max_length=255,
        widget=forms.widgets.TextInput(attrs={'class': 'form-control'}),
        label=_('Özgeçmiş')
    )
    sigara = forms.CharField(
        required=False,
        max_length=30,
        widget=forms.widgets.TextInput(attrs={'class': 'form-control'}),
        label=_('Sigara')
    )
    alkol = forms.CharField(
        required=False,
        max_length=30,
        widget=forms.widgets.TextInput(attrs={'class': 'form-control'}),
        label=_('Alkol')
    )
    boy = forms.IntegerField(
        required=False,
        widget=forms.widgets.NumberInput(attrs={'class': 'form-control'}),
        initial=0,
        label=_('Boy')
    )
    kilo = forms.IntegerField(
        required=False,
        widget=forms.widgets.NumberInput(attrs={'class': 'form-control'}),
        initial=0,
        label=_('Kilo')
    )

    class Meta:
        model = Hasta
        fields = '__all__'
