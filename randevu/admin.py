from django.contrib import admin
from randevu.models import Randevu


@admin.register(Randevu)
class Randevu(admin.ModelAdmin):
    list_display = (
        'hasta',
        'date',
        'time',
        'person_number',
        'state'
    )
    search_fields = ('hasta',)
