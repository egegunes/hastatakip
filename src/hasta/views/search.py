# -*- coding: utf-8 -*-

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import View
from django.template.response import TemplateResponse
from django.utils.text import slugify
from django.http import HttpResponseNotAllowed, HttpResponseBadRequest
from django.shortcuts import redirect

from hasta.models import Hasta


class HastaSearchView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        return HttpResponseNotAllowed(['GET'])

    def post(self, request, *args, **kwargs):
        if 'term' not in request.POST:
            return HttpResponseBadRequest()

        term = request.POST['term']

        try:
            term = int(term)
            try:
                hasta = Hasta.objects.get(tc_kimlik_no=term)
                return redirect(hasta)
            except (Hasta.MultipleObjectsReturned, Hasta.DoesNotExist) as e:
                qs = Hasta.objects.filter(tc_kimlik_no=term)
        except ValueError:
            qs = Hasta.objects.filter(slug__icontains=slugify(term))

        return TemplateResponse(
            request,
            'hasta/hasta_list.html',
            {'hasta_list': qs}
        )
