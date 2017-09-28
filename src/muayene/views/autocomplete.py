from dal import autocomplete

from muayene.models import Ilac, Laboratuvar


class IlacAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return Ilac.objects.none()

        queryset = Ilac.objects.all()

        if self.q:
            queryset = queryset.filter(ad__istartswith=self.q)

        return queryset


class LabAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return Laboratuvar.objects.none()

        queryset = Laboratuvar.objects.all()

        if self.q:
            queryset = queryset.filter(ad__istartswith=self.q)

        return queryset
