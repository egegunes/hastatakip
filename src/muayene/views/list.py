# -*- coding: utf-8 -*-

import datetime

from django.contrib.auth.mixins     import LoginRequiredMixin
from django.views.generic           import ListView
from django.http                    import HttpResponseNotAllowed

from muayene.models                 import Ilac, LaboratuvarIstek, MuayeneAlias

class IlacListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    model = Ilac
    context_object_name = 'ilac_list'
    queryset = Ilac.objects.all()

    def post(self, request, *args, **kwargs):
        return HttpResponseNotAllowed(['POST'])

class LastCreatedLabIstekView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    model = LaboratuvarIstek
    context_object_name = 'istek_list'
    today = datetime.date.today()
    twodaysago = today - datetime.timedelta(days=2)
    queryset = LaboratuvarIstek.objects.filter(tarih__gte=twodaysago, tarih__lte=today).order_by('-id')

    def post(self, request, *args, **kwargs):
        return HttpResponseNotAllowed(['POST'])

class MuayeneAliasListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    model = MuayeneAlias
    context_object_name = 'alias_list'
    queryset = MuayeneAlias.objects.all()

    def post(self, request, *args, **kwargs):
        return HttpResponseNotAllowed(['POST'])
