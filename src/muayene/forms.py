# -*- coding: utf-8 -*-

from django import forms
from django.utils.translation import ugettext_lazy as _

from dal import autocomplete

from muayene.models import Muayene, ReceteIlac


class MuayeneCreateForm(forms.ModelForm):
    class Meta:
        model = Muayene
        fields = '__all__'
        widgets = {
            'hasta': autocomplete.ModelSelect2(url='hasta:autocomplete', attrs={'style': 'width: 100%'}),
            'yakinma': forms.widgets.Textarea(attrs={'class': 'form-control', 'rows': '2'}),
            'kullandigi_ilaclar': forms.widgets.Textarea(attrs={'class': 'form-control', 'rows': '2'}),
            'baki': forms.widgets.Textarea(attrs={'class': 'form-control', 'rows': '2'}),
            'ontani_tani': forms.widgets.Textarea(attrs={'class': 'form-control', 'rows': '2'}),
            'oneri_gorusler': forms.widgets.Textarea(attrs={'class': 'form-control', 'rows': '2'}),
            'ozel_notlar': forms.widgets.Textarea(attrs={'class': 'form-control', 'rows': '2'})
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


class ReceteIlacForm(forms.ModelForm):
    class Meta:
        model = ReceteIlac
        fields = '__all__'
        widgets = {
            'ilac': forms.widgets.TextInput(attrs={'class': 'form-control'}),
            'kullanim': forms.widgets.TextInput(attrs={'class': 'form-control'}),
            'kutu': forms.widgets.NumberInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'ilac': _('İlaç'),
            'kullanim': _('Kullanım'),
            'kutu': _('Kutu'),
        }
