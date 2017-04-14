# -*- coding: utf-8 -*-

from django.contrib.auth.mixins     import LoginRequiredMixin
from django.views.generic.edit      import UpdateView

from muayene.models                 import Muayene, Ilac, Recete, Rapor, LaboratuvarIstek, MuayeneRelatedFile
from muayene.forms                  import MuayeneCreateForm, LaboratuvarIstekForm

class MuayeneUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    model = Muayene
    form_class = MuayeneCreateForm
