# -*- coding: utf-8 -*-

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

from hasta.models import Hasta

from muayene.models import Muayene, Recete, Rapor, LaboratuvarIstek, MuayeneRelatedFile


class HastaDetailView(LoginRequiredMixin, DetailView):
    login_url = "/login/"
    model = Hasta

    def get_context_data(self, **kwargs):
        context = super(HastaDetailView, self).get_context_data(**kwargs)

        hasta_slug = self.kwargs["slug"]

        context["muayene_list"] = Muayene.objects.filter(
            hasta__slug=hasta_slug
        ).order_by("-id")[:10]
        context["recete_list"] = Recete.objects.filter(hasta__slug=hasta_slug).order_by(
            "-id"
        )[:10]
        context["rapor_list"] = Rapor.objects.filter(hasta__slug=hasta_slug).order_by(
            "-id"
        )[:10]
        context["lab_list"] = LaboratuvarIstek.objects.filter(
            hasta__slug=hasta_slug
        ).order_by("-id")[:10]
        context["file_list"] = MuayeneRelatedFile.objects.filter(
            hasta__slug=hasta_slug
        ).order_by("-id")[:10]

        return context
