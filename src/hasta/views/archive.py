# -*- coding: utf-8 -*-

import datetime

from django.contrib.auth.mixins     import LoginRequiredMixin
from django.views.generic.dates     import View
from django.template.response       import TemplateResponse
from django.http                    import HttpResponseNotAllowed

from hasta.models                   import Hasta

class HastaLastCreatedView(LoginRequiredMixin, View):
    login_url = '/login/'
    template_name = 'hasta/hasta_list.html'

    def get(self, request, *args, **kwargs):
        today = datetime.date.today()
        yesterday = datetime.date.today() - datetime.timedelta(days=1)
        queryset = Hasta.objects.filter(kayit_tarihi__gte=yesterday, kayit_tarihi__lte=today)

        return TemplateResponse(request, self.template_name, {'hasta_list': queryset})

    def post(self, request, *args, **kwargs):
        return HttpResponseNotAllowed(['POST'])
