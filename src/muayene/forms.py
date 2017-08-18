# -*- coding: utf-8 -*-

from django import forms
from django.utils.translation import ugettext_lazy as _

from muayene.models import Muayene


class MuayeneCreateForm(forms.ModelForm):
    class Meta:
        model = Muayene
        fields = '__all__'
        widgets = {
            'hasta': forms.widgets.TextInput(attrs={'class': 'form-control'}),
            'yakinma': forms.widgets.TextInput(attrs={'class': 'form-control'}),
            'kullandigi_ilaclar': forms.widgets.TextInput(attrs={'class': 'form-control'}),
            'baki': forms.widgets.TextInput(attrs={'class': 'form-control'}),
            'ontani_tani': forms.widgets.TextInput(attrs={'class': 'form-control'}),
            'oneri_gorusler': forms.widgets.TextInput(attrs={'class': 'form-control'}),
            'ozel_notlar': forms.widgets.TextInput(attrs={'class': 'form-control'})
        }
        labels = {
            'hasta': _('Hasta'),
            'yakinma': _('Yakınma'),
            'kullandigi_ilaclar': _('Kullandığı ilaçlar'),
            'baki': _('Fizik bakı'),
            'ontani_tani': _('Öntanı / tanı'),
            'oneri_gorusler': _('Öneri ve görüşler'),
            'ozel_notlar': _('Özel notlar')
        }


class RaporCreateForm(forms.Form):
    tani = forms.CharField(
        max_length=255,
        required=True,
        widget=forms.widgets.TextInput(attrs={'class': 'form-control'}),
        label=_('Tanı')
    )
    gun = forms.IntegerField(
        required=True,
        widget=forms.widgets.NumberInput(attrs={'class': 'form-control'}),
        label=_('Gün')
    )


class DateRangeForm(forms.Form):
    start_date = forms.DateField(
        widget=forms.widgets.DateInput(
            attrs={
                'class': 'form-control datepicker input-sm',
                'name': 'start',
                'placeholder': 'Başlangıç tarihi'
            }
        ),
        required=True
    )
    end_date = forms.DateField(
        widget=forms.widgets.DateInput(
            attrs={
                'class': 'form-control datepicker input-sm',
                'name': 'end',
                'placeholder': 'Bitiş tarihi'
            }
        ),
        required=True
    )


class MuayeneRelatedFileForm(forms.Form):
    dosya = forms.FileField(
        required=True,
        widget=forms.widgets.FileInput(attrs={'class': 'form-control'}),
        label=_('Dosya'),
    )
