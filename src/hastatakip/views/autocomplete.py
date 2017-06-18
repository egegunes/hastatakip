# -*- coding: utf-8 -*-

import datetime

from django.contrib.auth.mixins         import LoginRequiredMixin
from django.utils.text                  import slugify
from django.urls                        import reverse

from dal                                import autocomplete

from hasta.models                       import Hasta
from muayene.models                     import Ilac


class HastaAutocomplete(LoginRequiredMixin, autocomplete.Select2QuerySetView):
    login_url = '/login/'

    def get_queryset(self):
        qs = Hasta.objects.all()

        if self.q:
            term = slugify(self.q)
            qs = qs.filter(slug__icontains=term)

        return qs
        
class IlacAutocomplete(LoginRequiredMixin, autocomplete.Select2QuerySetView):
    login_url = '/login/'

    def get_queryset(self):
        qs = Ilac.objects.all()

        if self.q:
            qs = qs.filter(ad__istartswith=self.q)

        return qs
