# -*- coding: utf-8 -*-

import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

from muayene.models import (
    Muayene,
    Ilac,
    Recete,
    Rapor,
    LaboratuvarIstek,
    MuayeneRelatedFile,
)
from muayene.forms import (
    ReceteCreateForm,
    RaporCreateForm,
    LaboratuvarIstekForm,
    MuayeneRelatedFileForm,
)


class MuayeneDetailView(LoginRequiredMixin, DetailView):
    """
    DetailView for muayene object.

    Context:

        recete_list: Recete entries created in relation with muayene object (filtered by muayene object's pk). Ordered by pk, decreasing. Showing 5 entries.
        rapor_list: Rapor entries created in relation with muayene object (filtered by muayene object's pk). Ordered by pk, decreasing. Showing 5 entries.
        lab_list: LaboratuvarIstek entries created in relation with muayene object (filtered by muayene object's pk). Ordered by pk, decreasing. Showing 5 entries.
        file_list: MuayeneRelatedFile entries created in relation with muayene object (filtered by muayene object's pk). Ordered by pk, decreasing. Showing 5 entries.

    URL: /muayene/<pk>
    """

    login_url = "/login/"
    model = Muayene

    def get_context_data(self, **kwargs):
        muayene_pk = self.kwargs["pk"]
        muayene = Muayene.objects.get(pk=muayene_pk)
        context = super(MuayeneDetailView, self).get_context_data(**kwargs)
        context["recete_list"] = Recete.objects.filter(muayene__pk=muayene_pk).order_by(
            "-pk"
        )[:5]
        context["rapor_list"] = Rapor.objects.filter(muayene__pk=muayene_pk).order_by(
            "-pk"
        )[:5]
        context["lab_list"] = LaboratuvarIstek.objects.filter(
            muayene__pk=muayene_pk
        ).order_by("-pk")[:5]
        context["file_list"] = MuayeneRelatedFile.objects.filter(
            muayene__pk=muayene_pk
        ).order_by("-pk")[:5]
        context["recete_form"] = ReceteCreateForm()
        context["rapor_form"] = RaporCreateForm()
        context["lab_form"] = LaboratuvarIstekForm()
        context["file_form"] = MuayeneRelatedFileForm()

        return context
