from django.contrib import admin

from muayene.models import Ilac, Recete, Muayene, LaboratuvarIstek, Rapor


class IlacAdmin(admin.ModelAdmin):
    list_display = ('id', 'ad', 'kullanim', 'bilgi')
    search_fields = ('ad',)


class ReceteAdmin(admin.ModelAdmin):
    list_display = ('id', 'tarih', 'hasta', 'muayene')
    readonly_fields = ('hasta', 'muayene')
    search_fields = ('hasta__ad', 'hasta__soyad')


class MuayeneAdmin(admin.ModelAdmin):
    list_display = ('id', 'tarih', 'hasta', 'yakinma', 'baki')
    readonly_fields = ('hasta',)
    search_fields = ('hasta__ad', 'hasta__soyad')


class LaboratuvarIstekAdmin(admin.ModelAdmin):
    list_display = ('id', 'tarih', 'hasta', 'muayene')
    readonly_fields = ('hasta', 'muayene')
    search_fields = ('hasta__ad', 'hasta__soyad')


class RaporAdmin(admin.ModelAdmin):
    list_display = ('id', 'tarih', 'hasta', 'muayene')
    readonly_fields = ('hasta', 'muayene')
    search_fields = ('hasta__ad', 'hasta__soyad')


admin.site.register(Ilac, IlacAdmin)
admin.site.register(Muayene, MuayeneAdmin)
admin.site.register(Recete, ReceteAdmin)
admin.site.register(LaboratuvarIstek, LaboratuvarIstekAdmin)
admin.site.register(Rapor, RaporAdmin)
