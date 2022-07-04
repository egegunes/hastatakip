# -*- coding: utf-8 -*-

from django.views.generic import View

from muayene.views import detail, form


class MuayeneBaseView(View):
    """
    According to request return different views.

    GET request:
        DetailView for muayene entry.

        URL: /muayene/<pk>
        <pk>: pk of muayene entry.

    POST request:
        DetailView have 4 different forms (recete, rapor, lab, file).
        Returns specific FormView according to submit type input's name.

        * get_kullanim is for ajax request used by ReceteFormView.
    """

    def get(self, request, *args, **kwargs):
        view = detail.MuayeneDetailView.as_view()

        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if "recete_form" in request.POST:
            view = form.ReceteFormView.as_view()
        elif "rapor_form" in request.POST:
            view = form.RaporFormView.as_view()
        elif "lab_form" in request.POST:
            view = form.LabIstekFormView.as_view()
        elif "file_form" in request.POST:
            view = form.FileUploadFormView.as_view()
        elif "get_kullanim" == request.POST.get("action", ""):
            view = form.GetIlacKullanimView.as_view()

        return view(request, *args, **kwargs)
