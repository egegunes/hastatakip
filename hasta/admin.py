from django.contrib import admin
from hasta.models import Hasta, Sozlesme


@admin.register(Hasta)
class Hasta(admin.ModelAdmin):
    list_display = (
        'ad',
        'soyad',
        'cinsiyet',
        'sigorta',
        'kayit_tarihi',
        'son_muayene_tarihi',
        'ahsevk_done',
        'ahsevk_done_tarih',
    )
    search_fields = ('ad', 'soyad', 'tc_kimlik_no')
    exclude = ('slug',)


@admin.register(Sozlesme)
class Sozlesme(admin.ModelAdmin):
    list_display = (
        'hasta',
        'baslangic_tarihi',
        'bitis_tarihi',
        'is_active',
        'days_left'
    )
    readonly_fields = ('hasta',)
