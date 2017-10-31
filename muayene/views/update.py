# -*- coding: utf-8 -*-

import logging

from django.views.generic import UpdateView
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import get_object_or_404

from muayene.models import Muayene, LaboratuvarIstek, Tetkik
from muayene.forms import MuayeneCreateForm, TetkikForm

logger = logging.getLogger(__name__)


class MuayeneUpdateView(UpdateView):
    model = Muayene
    form_class = MuayeneCreateForm


class LaboratuvarIstekUpdateView(UpdateView):
    model = LaboratuvarIstek
    fields = '__all__'
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        lab_id = self.kwargs.get('id')
        istek = LaboratuvarIstek.objects.get(pk=lab_id)
        tetkikler = istek.tetkikler.all()

        forms = [TetkikForm(
                    initial={
                        'laboratuvar': tetkik.laboratuvar,
                        'sonuc': tetkik.sonuc
                    },
                    instance=tetkik) for tetkik in tetkikler]

        context = dict(forms=forms)

        return super(LaboratuvarIstekUpdateView, self).get_context_data(**context)

    def post(self, request, *args, **kwargs):
        lab_id = self.kwargs.get('id')
        istek = LaboratuvarIstek.objects.get(pk=lab_id)
        tetkikler = istek.tetkikler.all()

        if not request.POST:
            return HttpResponseBadRequest()

        for lab, sonuc in request.POST.items():
            tetkik = tetkikler.get(laboratuvar__id=lab)
            tetkik.sonuc = sonuc
            tetkik.save()

        return HttpResponse(status=200)

