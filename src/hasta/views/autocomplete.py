from django.utils.text import slugify

from dal import autocomplete

from hasta.models import Hasta


class HastaAutocompleteView(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return Hasta.objects.none()

        queryset = Hasta.objects.all()

        if self.q:
            queryset = Hasta.objects.filter(slug__istartswith=slugify(self.q))

        return queryset
