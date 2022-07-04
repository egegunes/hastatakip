# -*- coding: utf-8 -*-

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView

from hasta.models import Hasta
from hasta.forms import HastaCreateForm


class HastaUpdateView(LoginRequiredMixin, UpdateView):
    login_url = "/login/"
    model = Hasta
    form_class = HastaCreateForm
