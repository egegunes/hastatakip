# -*- coding: utf-8 -*-

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import View
from django.template.response import TemplateResponse
from django.utils.text import slugify
from django.http import HttpResponseNotAllowed

from hasta.models import Hasta


class HastaSearchView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        return HttpResponseNotAllowed(['GET'])

    def post(self, request, *args, **kwargs):

        if 'term' in request.POST:
            slug = slugify(request.POST['term'])

            qs = Hasta.objects.filter(slug__icontains=slug)

            return TemplateResponse(request, 'hasta/hasta_list.html', {'hasta_list': qs})
