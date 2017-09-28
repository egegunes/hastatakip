# -*- coding: utf-8 -*-

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

from muayene.models import Muayene, Recete, Rapor, LaboratuvarIstek, MuayeneRelatedFile, Laboratuvar
from muayene.forms import ReceteIlacForm, RaporCreateForm, MuayeneRelatedFileForm, CustomLabForm


class MuayeneDetailView(LoginRequiredMixin, DetailView):
    model = Muayene

    def get_context_data(self, **kwargs):
        context = super(MuayeneDetailView, self).get_context_data(**kwargs)
        context['recete_list'] = Recete.objects.filter(muayene__pk=self.kwargs['pk']).order_by('-pk')[:5]
        context['rapor_list'] = Rapor.objects.filter(muayene__pk=self.kwargs['pk']).order_by('-pk')[:5]
        context['lab_list'] = LaboratuvarIstek.objects.filter(muayene__pk=self.kwargs['pk']).order_by('-pk')[:5]
        context['file_list'] = MuayeneRelatedFile.objects.filter(muayene__pk=self.kwargs['pk']).order_by('-pk')[:5]
        context['recete_form'] = ReceteIlacForm()
        context['lab_form'] = CustomLabForm()
        context['rapor_form'] = RaporCreateForm()
        context['file_form'] = MuayeneRelatedFileForm()

        return context
