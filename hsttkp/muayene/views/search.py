# -*- coding: utf-8 -*-

from django.contrib.auth.mixins     import LoginRequiredMixin
from django.views.generic.base      import View
from django.template.response       import TemplateResponse
from django.http                    import HttpResponseNotAllowed

from muayene.models                 import Ilac

class IlacSearchView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        return HttpResponseNotAllowed(['GET'])

    def post(self, request, *args, **kwargs):

        if 'term' in request.POST:
            term = request.POST['term']

            qs = Ilac.objects.filter(ad__icontains = term)

            return TemplateResponse(request, 'muayene/ilac_list.html', {'ilac_list': qs})
