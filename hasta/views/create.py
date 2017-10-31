# -*- coding: utf-8 -*-

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, View
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponseNotAllowed

from hasta.models import Hasta, Sozlesme
from hasta.forms import HastaCreateForm


class HastaCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    model = Hasta
    form_class = HastaCreateForm


class SozlesmeCreateView(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request, *args, **kwargs):
        return HttpResponseNotAllowed(['GET'])

    def post(self, request, *args, **kwargs):
        slug = self.kwargs['slug']
        hasta = Hasta.objects.get(slug=slug)

        Sozlesme.objects.create(hasta=hasta, is_active=True)

        return HttpResponseRedirect(reverse('hasta:detail', kwargs={'slug': slug}))
