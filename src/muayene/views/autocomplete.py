from dal import autocomplete

from muayene.models import Ilac


class IlacAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return Ilac.objects.none()

        queryset = Ilac.objects.all()

        if self.q:
            queryset = queryset.filter(ad__istartswith=self.q)

        return queryset

