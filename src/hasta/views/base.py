# -*- coding: utf-8 -*-

from django.views.generic import View

from hasta.views import detail, create


class HastaDetailBaseView(View):
    def get(self, request, *args, **kwargs):
        view = detail.HastaDetailView.as_view()

        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if "sozlesme" in request.POST:
            view = create.SozlesmeCreateView.as_view()

        return view(request, *args, **kwargs)
