# -*- coding: utf-8 -*-

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.http import HttpResponseNotAllowed

from hasta.models import Hasta, Sozlesme

from muayene.models import Muayene, Recete, Rapor, LaboratuvarIstek, MuayeneRelatedFile


class HastaListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    context_object_name = 'hasta_list'
    queryset = Hasta.objects.order_by('soyad')
    paginate_by = 25

    def get_context_data(self):
        context = super(HastaListView, self).get_context_data()
        hasta_count = Hasta.objects.all().count()
        context['hasta_count'] = hasta_count

        return context

    def post(self, request, *args, **kwargs):
        return HttpResponseNotAllowed(['POST'])


class SozlesmeListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    context_object_name = 'sozlesme_list'
    queryset = Sozlesme.objects.order_by('-baslangic_tarihi')
    template_name = 'hasta/sozlesme_list.html'

    def get_context_data(self):
        context = super(SozlesmeListView, self).get_context_data()
        hasta_count = Sozlesme.objects.filter(is_active=True).count()
        context['hasta_count'] = hasta_count

        return context

    def post(self, request, *args, **kwargs):
        return HttpResponseNotAllowed(['POST'])


class MuayeneListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    context_object_name = 'muayene_list'

    def get_queryset(self):
        hasta_slug = self.kwargs['slug']
        return Muayene.objects.filter(hasta__slug=hasta_slug).order_by('-id')

    def post(self, request, *args, **kwargs):
        return HttpResponseNotAllowed(['POST'])


class ReceteListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    context_object_name = 'recete_list'

    def get_queryset(self):
        hasta_slug = self.kwargs['slug']
        return Recete.objects.filter(hasta__slug=hasta_slug).order_by('-id')

    def post(self, request, *args, **kwargs):
        return HttpResponseNotAllowed(['POST'])


class RaporListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    context_object_name = 'rapor_list'

    def get_queryset(self):
        hasta_slug = self.kwargs['slug']
        return Rapor.objects.filter(hasta__slug=hasta_slug).order_by('-id')

    def post(self, request, *args, **kwargs):
        return HttpResponseNotAllowed(['POST'])


class LabIstekListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    context_object_name = 'istek_list'

    def get_queryset(self):
        hasta_slug = self.kwargs['slug']
        return LaboratuvarIstek.objects.filter(hasta__slug=hasta_slug).order_by('-id')

    def post(self, request, *args, **kwargs):
        return HttpResponseNotAllowed(['POST'])


class DosyaListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    context_object_name = 'file_list'

    def get_queryset(self):
        hasta_slug = self.kwargs['slug']
        return MuayeneRelatedFile.objects.filter(hasta__slug=hasta_slug).order_by('-id')

    def post(self, request, *args, **kwargs):
        return HttpResponseNotAllowed(['POST'])


class HastaEpikrizView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    context_object_name = 'muayene_list'
    template_name = 'hasta/epikriz.html'
    paginate_by = 5

    def get_queryset(self):
        hasta_slug = self.kwargs['slug']
        return Muayene.objects.filter(hasta__slug=hasta_slug).order_by('-id')

    def get_context_data(self, **kwargs):
        context = super(HastaEpikrizView, self).get_context_data(**kwargs)
        hasta_slug = self.kwargs['slug']
        context['hasta'] = Hasta.objects.get(slug=hasta_slug)

        return context

    def post(self, request, *args, **kwargs):
        return HttpResponseNotAllowed(['POST'])
