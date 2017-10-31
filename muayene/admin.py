from django.contrib import admin
from muayene.models import Muayene, Recete, Rapor, Laboratuvar, LaboratuvarIstek, Ilac


@admin.register(Muayene)
class Muayene(admin.ModelAdmin):
    list_display = (
        'hasta',
        'tarih',
        'yakinma',
        'baki',
        'ontani_tani'
    )
    search_fields = ('hasta__ad', 'hasta__soyad', 'hasta__tc_kimlik_no')
    readonly_fields = ('hasta',)


@admin.register(Ilac)
class Ilac(admin.ModelAdmin):
    list_display = (
        'ad',
        'kullanim',
        'bilgi'
    )
    search_fields = ('ad',)


@admin.register(Recete)
class Recete(admin.ModelAdmin):
    list_display = (
        'hasta',
        'tarih'
    )
    search_fields = ('hasta__ad', 'hasta__soyad', 'hasta__tc_kimlik_no')
    readonly_fields = ('hasta', 'muayene', 'ilaclar')


@admin.register(Rapor)
class Rapor(admin.ModelAdmin):
    list_display = (
        'hasta',
        'tarih',
        'tani',
        'gun'
    )
    search_fields = ('hasta__ad', 'hasta__soyad', 'hasta__tc_kimlik_no')
    readonly_fields = ('hasta', 'muayene', 'tani', 'gun')


@admin.register(Laboratuvar)
class Laboratuvar(admin.ModelAdmin):
    search_fields = ('ad',)


@admin.register(LaboratuvarIstek)
class LaboratuvarIstek(admin.ModelAdmin):
    list_display = (
        'hasta',
        'tarih'
    )
    search_fields = ('hasta__ad', 'hasta__soyad', 'hasta__tc_kimlik_no')
    readonly_fields = ('hasta', 'muayene', 'tetkikler')
