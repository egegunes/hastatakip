# -*- coding: utf-8 -*-

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView


class MainIndexView(LoginRequiredMixin, TemplateView):
    template_name = "hastatakip/index.html"
