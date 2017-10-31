# -*- coding: utf-8 -*-

import json, datetime

from django.views.generic.detail    import SingleObjectMixin
from django.contrib.auth.mixins     import LoginRequiredMixin
from django.core.urlresolvers       import reverse
from django.template.response       import TemplateResponse
from django.views.generic.base      import View
from django.views.generic           import FormView
from django.http                    import HttpResponseForbidden, HttpResponse

from muayene.forms import (
    RaporCreateForm,
    MuayeneRelatedFileForm
)
from muayene.models import (
    Ilac,
    Muayene,
    Rapor,
    MuayeneRelatedFile
)


class RaporFormView(SingleObjectMixin, FormView):
    """
    FormView for creating Rapor objects in relation with specific Muayene object.

    hasta, muayene and tarih fields provided automatically from Muayene object,
    so those did not displayed to user.  tani and gun fields are required,
    without those form will be invalid. This functionality is configured in
    muayene.forms.RaporCreateForm.

    On success page redirects to MuayeneDetailView, which is the same page but
    created Rapor object will be displayed in rapor_list. 
    """

    form_class = RaporCreateForm
    model = Muayene

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return HttpResponseForbidden()
        self.object = self.get_object()
        form = self.form_class(request.POST)
        if form.is_valid():
            rapor = Rapor(hasta=self.object.hasta, 
                    muayene=self.object, 
                    tarih=datetime.date.today(),
                    tani=form.cleaned_data['tani'], 
                    gun=form.cleaned_data['gun'])
            rapor.save()
        return super(RaporFormView, self).post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('muayene:detail', kwargs={'pk': self.object.pk})


class FileUploadFormView(SingleObjectMixin, FormView):
    template_name = 'muayene/muayene_detail.html'
    form_class = MuayeneRelatedFileForm
    model = Muayene

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return HttpResponseForbidden()

        self.object = self.get_object()
        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():
            newfile = MuayeneRelatedFile(hasta=self.object.hasta, muayene=self.object, dosya=request.FILES['dosya'])
            newfile.save()
        return super(FileUploadFormView, self).post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('muayene:detail', kwargs={'pk': self.object.pk})


class GetIlacKullanimView(View):
    """
    The view is used for ajax request. Whenever user choose an Ilac object from
    dal's select2 field an ajax request has been made with object's id. By this
    request this view get the specific object and returns 'kullanim' field to
    be shown to user in recete_form.
    """

    def post(self, request, *args, **kwargs):
        if self.request.is_ajax() and request.user.is_authenticated():
            return self.ajax(request)
        else:
            return HttpResponseForbidden()

    def ajax(self, request):
        response_dict = {
            'success': True,
        }

        ilac_id = request.POST.get('ilac', '')
        ilac = Ilac.objects.get(pk=ilac_id)

        response_dict = {
            'kullanim': ilac.kullanim
        }

        return HttpResponse(json.dumps(response_dict))
