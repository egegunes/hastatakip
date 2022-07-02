# -*- coding: utf-8 -*-

import json, datetime

from django.views.generic.detail    import SingleObjectMixin
from django.contrib.auth.mixins     import LoginRequiredMixin
from django.urls       import reverse
from django.template.response       import TemplateResponse
from django.views.generic.base      import View
from django.views.generic           import FormView
from django.http                    import HttpResponseForbidden, HttpResponse

from muayene.forms import (
    ReceteCreateForm,
    RaporCreateForm,
    LaboratuvarIstekForm,
    MuayeneRelatedFileForm
)
from muayene.models import (
    Ilac,
    Muayene,
    Recete,        
    Rapor,
    LaboratuvarIstek,
    MuayeneRelatedFile
)

class ReceteFormView(SingleObjectMixin, FormView):
    """
    FormView for creating Recete objects in relation with specific Muayene object.
    
    hasta, muayene and tarih fields provided automatically from Muayene object, so those did not displayed to user.
    ilac1, ilac1_kullanim, ilac1_kutu is required, without those form will be invalid. This functionality is configured in muayene.forms.ReceteCreateForm.
    Other fields are not mandatory. Those can be blank or null, form will be valid anyway.

    On success page redirects to MuayeneDetailView, which is the same page but created Recete object will be shown in recete_list.
    """

    form_class = ReceteCreateForm
    model = Muayene

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return HttpResponseForbidden()
        self.object = self.get_object()
        form = self.form_class(request.POST)
        if form.is_valid():
            recete = Recete(hasta=self.object.hasta, 
                            muayene=self.object, 
                            tarih=datetime.date.today(),
                            ilac1=form.cleaned_data['ilac1'],
                            ilac1_kullanim=form.cleaned_data['ilac1_kullanim'],
                            ilac1_kutu=form.cleaned_data['ilac1_kutu'],
                            ilac2=form.cleaned_data['ilac2'],
                            ilac2_kullanim=form.cleaned_data['ilac2_kullanim'],
                            ilac2_kutu=form.cleaned_data['ilac2_kutu'],
                            ilac3=form.cleaned_data['ilac3'],
                            ilac3_kullanim=form.cleaned_data['ilac3_kullanim'],
                            ilac3_kutu=form.cleaned_data['ilac3_kutu'],
                            ilac4=form.cleaned_data['ilac4'],
                            ilac4_kullanim=form.cleaned_data['ilac4_kullanim'],
                            ilac4_kutu=form.cleaned_data['ilac4_kutu'],
                            ilac5=form.cleaned_data['ilac5'],
                            ilac5_kullanim=form.cleaned_data['ilac5_kullanim'],
                            ilac5_kutu=form.cleaned_data['ilac5_kutu'])
            recete.save()

        return super(ReceteFormView, self).post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('muayene:detail', kwargs={'pk': self.object.pk})

class RaporFormView(SingleObjectMixin, FormView):
    """
    FormView for creating Rapor objects in relation with specific Muayene object.
    
    hasta, muayene and tarih fields provided automatically from Muayene object, so those did not displayed to user.
    tani and gun fields are required, without those form will be invalid. This functionality is configured in muayene.forms.RaporCreateForm.

    On success page redirects to MuayeneDetailView, which is the same page but created Rapor object will be displayed in rapor_list.
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

class LabIstekFormView(SingleObjectMixin, FormView):
    """
    FormView for creating LaboratuvarIstek objects in relation with specific
    Muayene object.
    
    hasta, muayene and tarih fields provided automatically from Muayene object,
    so those did not displayed to user. There is no required field in this
    field, so user can create a LaboratuvarIstek object with no input. At this
    time only option is trusting user to not do that.

    There is two ways to create new LaboratuvarIstek object:
    
    First way is let the user choose fields by checkboxes in lab_form. On
    success, page redirects to MuayeneDetailView, which is the same page but
    created LaboratuvarIstek object will be displayed in lab_list.
    
    And the second way is making a AHSevk request. AHSevk is a special form of
    creating LaboratuvarIstek objects and fields determined by patient's age.
    User have no control on the fields because they're pre-determined. On
    success, page redirects to AHSevkPrintView which creates the AHSevk pdf
    file for printing and shows it.
    """

    template_name = 'muayene/muayene_detail.html'
    form_class = LaboratuvarIstekForm
    model = Muayene

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return HttpResponseForbidden()
        self.object = self.get_object()
        self.request = request
        if 'ahsevk' not in request.POST:
            form = self.form_class(request.POST)
        else:
            yas = request.POST['yas']
            yas = int(yas)
            if yas < 18:
                data = {
                    'hemogram': True,
                    'sedim': True,
                    'tam_idrar': True
                }
            elif yas >= 18 and yas < 40:
                data = {
                    'hemogram': True,
                    'sedim': True,
                    'tam_idrar': True,
                    'aclik_kan': True,
                    'total_kolesterol': True,
                    'hdl': True,
                    'kreatinin': True,
                    'sgot': True,
                    'sgpt': True,
                    'ekg': True,
                    'pa_akciger': True
                }
            elif yas >= 40:
                data = {
                    'hemogram': True,
                    'sedim': True,
                    'tam_idrar': True,
                    'aclik_kan': True,
                    'total_kolesterol': True,
                    'hdl': True,
                    'ldl': True,
                    'kreatinin': True,
                    'sgot': True,
                    'urik_asit': True,
                    'sgpt': True,
                    'ekg': True,
                    'pa_akciger': True
                }

            hasta = self.object.hasta
            hasta.ahsevk_done = True
            hasta.ahsevk_done_tarih = datetime.date.today()
            hasta.save()

            if hasta.ahsevk_done is not True:
                hasta.ahsevk_done = True
                hasta.save()

            form = self.form_class(data)
        if form.is_valid():
            lab_istek = LaboratuvarIstek(hasta=self.object.hasta,
                                         muayene=self.object, 
                                         tarih=datetime.date.today(), 
                                         hemogram=form.cleaned_data['hemogram'],
                                         sedim=form.cleaned_data['sedim'],
                                         serum_demir=form.cleaned_data['serum_demir'],
                                         tdbk=form.cleaned_data['tdbk'],
                                         ferritin=form.cleaned_data['ferritin'],
                                         b12=form.cleaned_data['b12'],
                                         folik_asit=form.cleaned_data['folik_asit'],
                                         hemoglobin=form.cleaned_data['hemoglobin'],
                                         aclik_kan=form.cleaned_data['aclik_kan'],
                                         tokluk_kan=form.cleaned_data['tokluk_kan'],
                                         hba1c=form.cleaned_data['hba1c'],
                                         sgot=form.cleaned_data['sgot'],
                                         sgpt=form.cleaned_data['sgpt'],
                                         ggt=form.cleaned_data['ggt'],
                                         alp=form.cleaned_data['alp'],
                                         ure=form.cleaned_data['ure'],
                                         kreatinin=form.cleaned_data['kreatinin'],
                                         urik_asit=form.cleaned_data['urik_asit'],
                                         total_kolesterol=form.cleaned_data['total_kolesterol'],
                                         hdl=form.cleaned_data['hdl'],
                                         trigliserit=form.cleaned_data['trigliserit'],
                                         ldl=form.cleaned_data['ldl'],
                                         free_t3=form.cleaned_data['free_t3'],
                                         free_t4=form.cleaned_data['free_t4'],
                                         tsh=form.cleaned_data['tsh'],
                                         anti_tpo=form.cleaned_data['anti_tpo'],
                                         anti_tg=form.cleaned_data['anti_tg'],
                                         aso=form.cleaned_data['aso'],
                                         crp=form.cleaned_data['crp'],
                                         rf=form.cleaned_data['rf'],
                                         psa=form.cleaned_data['psa'],
                                         free_psa=form.cleaned_data['free_psa'],
                                         tam_idrar=form.cleaned_data['tam_idrar'],
                                         idrar_kab=form.cleaned_data['idrar_kab'],
                                         gaita=form.cleaned_data['gaita'],
                                         bogaz_kab=form.cleaned_data['bogaz_kab'],
                                         ejaculat_kab=form.cleaned_data['ejaculat_kab'],
                                         ekg=form.cleaned_data['ekg'],
                                         eforlu_ekg=form.cleaned_data['eforlu_ekg'],
                                         ekokardiografi=form.cleaned_data['ekokardiografi'],
                                         tansiyon_holter=form.cleaned_data['tansiyon_holter'],
                                         ekg_holter=form.cleaned_data['ekg_holter'],
                                         pa_akciger=form.cleaned_data['pa_akciger'],
                                         waters=form.cleaned_data['waters'],
                                         ikiyonlu_servikal=form.cleaned_data['ikiyonlu_servikal'],
                                         ikiyonlu_lsv=form.cleaned_data['ikiyonlu_lsv'],
                                         tum_batin=form.cleaned_data['tum_batin'],
                                         ust_batin=form.cleaned_data['ust_batin'],
                                         alt_batin=form.cleaned_data['alt_batin'],
                                         uriner=form.cleaned_data['uriner'],
                                         tiroid=form.cleaned_data['tiroid'],
                                         meme=form.cleaned_data['meme'],
                                         aclik_insulin=form.cleaned_data['aclik_insulin'],
                                         yuzyirmi_insulin=form.cleaned_data['yuzyirmi_insulin'],
                                         yirmibesohd=form.cleaned_data['yirmibesohd'],
                                         og11=form.cleaned_data['og11'],
                                         custom1=form.cleaned_data['custom1'],
                                         custom1_ad=form.cleaned_data['custom1_ad'],
                                         custom2=form.cleaned_data['custom2'],
                                         custom2_ad=form.cleaned_data['custom2_ad'],
                                         custom3=form.cleaned_data['custom3'],
                                         custom3_ad=form.cleaned_data['custom3_ad'],
                                         custom4=form.cleaned_data['custom4'],
                                         custom4_ad=form.cleaned_data['custom4_ad'],
                                         custom5=form.cleaned_data['custom5'],
                                         custom5_ad=form.cleaned_data['custom5_ad'],)
            lab_istek.save()

        return super(LabIstekFormView, self).post(request, *args, **kwargs)

    def get_success_url(self):
        if 'ahsevk' not in self.request.POST:
            return reverse('muayene:detail', kwargs={'pk': self.object.pk})
        else:
            return reverse('muayene:ahsevk', kwargs={'pk': self.object.pk}) 

class LabSonucFormView(LoginRequiredMixin, FormView):
    """
    FormView for updating LaboratuvarIstek objects.

    Initial data provided for displaying specific fields to user.
    For instance:
        if istek.hemogram is True:
            show hemogram_sonuc field
    """

    template_name = 'muayene/laboratuvaristek_form.html'
    form_class = LaboratuvarIstekForm

    def get(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        istek = LaboratuvarIstek.objects.get(pk=pk)
        initial_data = {
            'hemogram': istek.hemogram,
            'hemogram_sonuc': istek.hemogram_sonuc,
            'sedim': istek.sedim,
            'sedim_sonuc': istek.sedim_sonuc,
            'serum_demir': istek.serum_demir,
            'serum_demir_sonuc': istek.serum_demir_sonuc,
            'tdbk': istek.tdbk,
            'tdbk_sonuc': istek.tdbk_sonuc,
            'ferritin': istek.ferritin,
            'ferritin_sonuc': istek.ferritin_sonuc,
            'b12': istek.b12,
            'b12_sonuc': istek.b12_sonuc,
            'folik_asit': istek.folik_asit,
            'folik_asit_sonuc': istek.folik_asit_sonuc,
            'hemoglobin': istek.hemoglobin,
            'hemoglobin_sonuc': istek.hemoglobin_sonuc,
            'aclik_kan': istek.aclik_kan,
            'aclik_kan_sonuc': istek.aclik_kan_sonuc,
            'tokluk_kan': istek.tokluk_kan,
            'tokluk_kan_sonuc': istek.tokluk_kan_sonuc,
            'hba1c': istek.hba1c,
            'hba1c_sonuc': istek.hba1c_sonuc,
            'sgot': istek.sgot,
            'sgot_sonuc': istek.sgot_sonuc,
            'sgpt': istek.sgpt,
            'sgpt_sonuc': istek.sgpt_sonuc,
            'ggt': istek.ggt,
            'ggt_sonuc': istek.ggt_sonuc,
            'alp': istek.alp,
            'alp_sonuc': istek.alp_sonuc,
            'ure': istek.ure,
            'ure_sonuc': istek.ure_sonuc,
            'kreatinin': istek.kreatinin,
            'kreatinin_sonuc': istek.kreatinin_sonuc,
            'urik_asit': istek.urik_asit,
            'urik_asit_sonuc': istek.urik_asit_sonuc,
            'total_kolesterol': istek.total_kolesterol,
            'total_kolesterol_sonuc': istek.total_kolesterol_sonuc,
            'hdl': istek.hdl,
            'hdl_sonuc': istek.hdl_sonuc,
            'trigliserit': istek.trigliserit,
            'trigliserit_sonuc': istek.trigliserit_sonuc,
            'ldl': istek.ldl,
            'ldl_sonuc': istek.ldl_sonuc,
            'free_t3': istek.free_t3,
            'free_t3_sonuc': istek.free_t3_sonuc,
            'free_t4': istek.free_t4,
            'free_t4_sonuc': istek.free_t4_sonuc,
            'tsh': istek.tsh,
            'tsh_sonuc': istek.tsh_sonuc,
            'anti_tpo': istek.anti_tpo,
            'anti_tpo_sonuc': istek.anti_tpo_sonuc,
            'anti_tg': istek.anti_tg,
            'anti_tg_sonuc': istek.anti_tg_sonuc,
            'aso': istek.aso,
            'aso_sonuc': istek.aso_sonuc,
            'crp': istek.crp,
            'crp_sonuc': istek.crp_sonuc,
            'rf': istek.rf,
            'rf_sonuc': istek.rf_sonuc,
            'psa': istek.psa,
            'psa_sonuc': istek.psa_sonuc,
            'free_psa': istek.free_psa,
            'free_psa_sonuc': istek.free_psa_sonuc,
            'tam_idrar': istek.tam_idrar,
            'tam_idrar_sonuc': istek.tam_idrar_sonuc,
            'idrar_kab': istek.idrar_kab,
            'idrar_kab_sonuc': istek.idrar_kab_sonuc,
            'gaita': istek.gaita,
            'gaita_sonuc': istek.gaita_sonuc,
            'bogaz_kab': istek.bogaz_kab,
            'bogaz_kab_sonuc': istek.bogaz_kab_sonuc,
            'ejaculat_kab': istek.ejaculat_kab,
            'ejaculat_kab_sonuc': istek.ejaculat_kab_sonuc,
            'ekg': istek.ekg,
            'ekg_sonuc': istek.ekg_sonuc,
            'eforlu_ekg': istek.eforlu_ekg,
            'eforlu_ekg_sonuc': istek.eforlu_ekg_sonuc,
            'ekokardiografi': istek.ekokardiografi,
            'ekokardiografi_sonuc': istek.ekokardiografi_sonuc,
            'tansiyon_holter': istek.tansiyon_holter,
            'tansiyon_holter_sonuc': istek.tansiyon_holter_sonuc,
            'ekg_holter': istek.ekg_holter,
            'ekg_holter_sonuc': istek.ekg_holter_sonuc,
            'pa_akciger': istek.pa_akciger,
            'pa_akciger_sonuc': istek.pa_akciger_sonuc,
            'waters': istek.waters,
            'waters_sonuc': istek.waters_sonuc,
            'ikiyonlu_servikal': istek.ikiyonlu_servikal,
            'ikiyonlu_servikal_sonuc': istek.ikiyonlu_servikal_sonuc,
            'ikiyonlu_lsv': istek.ikiyonlu_lsv,
            'ikiyonlu_lsv_sonuc': istek.ikiyonlu_lsv_sonuc,
            'tum_batin': istek.tum_batin,
            'tum_batin_sonuc': istek.tum_batin_sonuc,
            'ust_batin': istek.ust_batin,
            'ust_batin_sonuc': istek.ust_batin_sonuc,
            'alt_batin': istek.alt_batin,
            'alt_batin_sonuc': istek.alt_batin_sonuc,
            'uriner': istek.uriner,
            'uriner_sonuc': istek.uriner_sonuc,
            'tiroid': istek.tiroid,
            'tiroid_sonuc': istek.tiroid_sonuc,
            'meme': istek.meme,
            'meme_sonuc': istek.meme_sonuc,
            'tiroid_sintigrafi': istek.tiroid_sintigrafi,
            'tiroid_sintigrafi_sonuc': istek.tiroid_sintigrafi_sonuc,
            'aclik_insulin': istek.aclik_insulin,
            'aclik_insulin_sonuc': istek.aclik_insulin_sonuc,
            'yuzyirmi_insulin': istek.yuzyirmi_insulin,
            'yuzyirmi_insulin_sonuc': istek.yuzyirmi_insulin_sonuc,
            'yirmibesohd': istek.yirmibesohd,
            'yirmibesohd_sonuc': istek.yirmibesohd_sonuc,
            'og11': istek.og11,
            'og11_sonuc': istek.og11_sonuc,
            'custom1': istek.custom1,
            'custom1_ad': istek.custom1_ad,
            'custom1_sonuc': istek.custom1_sonuc,
            'custom2': istek.custom2,
            'custom2_ad': istek.custom2_ad,
            'custom2_sonuc': istek.custom2_sonuc,
            'custom3': istek.custom3,
            'custom3_ad': istek.custom3_ad,
            'custom3_sonuc': istek.custom3_sonuc,
            'custom4': istek.custom4,
            'custom4_ad': istek.custom4_ad,
            'custom4_sonuc': istek.custom4_sonuc,
            'custom5': istek.custom5,
            'custom5_ad': istek.custom5_ad,
            'custom5_sonuc': istek.custom5_sonuc,
        }
        form = self.form_class(initial=initial_data)
        context = {
            'form': form
        }

        return TemplateResponse(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        istek = LaboratuvarIstek.objects.get(pk=pk)

        form = self.form_class(request.POST)

        if form.is_valid():
            istek.hemogram_sonuc = form.cleaned_data['hemogram_sonuc']
            istek.sedim_sonuc = form.cleaned_data['sedim_sonuc']
            istek.serum_demir_sonuc = form.cleaned_data['serum_demir_sonuc']
            istek.tdbk_sonuc = form.cleaned_data['tdbk_sonuc']
            istek.ferritin_sonuc = form.cleaned_data['ferritin_sonuc']
            istek.b12_sonuc = form.cleaned_data['b12_sonuc']
            istek.folik_asit_sonuc = form.cleaned_data['folik_asit_sonuc']
            istek.hemoglobin_sonuc = form.cleaned_data['hemoglobin_sonuc']
            istek.aclik_kan_sonuc = form.cleaned_data['aclik_kan_sonuc']
            istek.tokluk_kan_sonuc = form.cleaned_data['tokluk_kan_sonuc']
            istek.hba1c_sonuc = form.cleaned_data['hba1c_sonuc']
            istek.sgot_sonuc = form.cleaned_data['sgot_sonuc']
            istek.sgpt_sonuc = form.cleaned_data['sgpt_sonuc']
            istek.ggt_sonuc = form.cleaned_data['ggt_sonuc']
            istek.alp_sonuc = form.cleaned_data['alp_sonuc']
            istek.ure_sonuc = form.cleaned_data['ure_sonuc']
            istek.kreatinin_sonuc = form.cleaned_data['kreatinin_sonuc']
            istek.urik_asit_sonuc = form.cleaned_data['urik_asit_sonuc']
            istek.total_kolesterol_sonuc = form.cleaned_data['total_kolesterol_sonuc']
            istek.hdl_sonuc = form.cleaned_data['hdl_sonuc']
            istek.trigliserit_sonuc = form.cleaned_data['trigliserit_sonuc']
            istek.ldl_sonuc = form.cleaned_data['ldl_sonuc']
            istek.free_t3_sonuc = form.cleaned_data['free_t3_sonuc']
            istek.free_t4_sonuc = form.cleaned_data['free_t4_sonuc']
            istek.tsh_sonuc = form.cleaned_data['tsh_sonuc']
            istek.anti_tpo_sonuc = form.cleaned_data['anti_tpo_sonuc']
            istek.anti_tg_sonuc = form.cleaned_data['anti_tg_sonuc']
            istek.aso_sonuc = form.cleaned_data['aso_sonuc']
            istek.crp_sonuc = form.cleaned_data['crp_sonuc']
            istek.rf_sonuc = form.cleaned_data['rf_sonuc']
            istek.psa_sonuc = form.cleaned_data['psa_sonuc']
            istek.free_psa_sonuc = form.cleaned_data['free_psa_sonuc']
            istek.tam_idrar_sonuc = form.cleaned_data['tam_idrar_sonuc']
            istek.idrar_kab_sonuc = form.cleaned_data['idrar_kab_sonuc']
            istek.gaita_sonuc = form.cleaned_data['gaita_sonuc']
            istek.bogaz_kab_sonuc = form.cleaned_data['bogaz_kab_sonuc']
            istek.ejaculat_kab_sonuc = form.cleaned_data['ejaculat_kab_sonuc']
            istek.ekg_sonuc = form.cleaned_data['ekg_sonuc']
            istek.eforlu_ekg_sonuc = form.cleaned_data['eforlu_ekg_sonuc']
            istek.ekokardiografi_sonuc = form.cleaned_data['ekokardiografi_sonuc']
            istek.tansiyon_holter_sonuc = form.cleaned_data['tansiyon_holter_sonuc']
            istek.ekg_holter_sonuc = form.cleaned_data['ekg_holter_sonuc']
            istek.pa_akciger_sonuc = form.cleaned_data['pa_akciger_sonuc']
            istek.waters_sonuc = form.cleaned_data['waters_sonuc']
            istek.ikiyonlu_servikal_sonuc = form.cleaned_data['ikiyonlu_servikal_sonuc']
            istek.ikiyonlu_lsv_sonuc = form.cleaned_data['ikiyonlu_lsv_sonuc']
            istek.tum_batin_sonuc = form.cleaned_data['tum_batin_sonuc']
            istek.ust_batin_sonuc = form.cleaned_data['ust_batin_sonuc']
            istek.alt_batin_sonuc = form.cleaned_data['alt_batin_sonuc']
            istek.uriner_sonuc = form.cleaned_data['uriner_sonuc']
            istek.tiroid_sonuc = form.cleaned_data['tiroid_sonuc']
            istek.meme_sonuc = form.cleaned_data['meme_sonuc']
            istek.tiroid_sintigrafi_sonuc = form.cleaned_data['tiroid_sintigrafi_sonuc']
            istek.aclik_insulin_sonuc = form.cleaned_data['aclik_insulin_sonuc']
            istek.yuzyirmi_insulin_sonuc = form.cleaned_data['yuzyirmi_insulin_sonuc']
            istek.yirmibesohd_sonuc = form.cleaned_data['yirmibesohd_sonuc']
            istek.og11_sonuc = form.cleaned_data['og11_sonuc']
            istek.custom1_sonuc = form.cleaned_data['custom1_sonuc']
            istek.custom2_sonuc = form.cleaned_data['custom2_sonuc']
            istek.custom3_sonuc = form.cleaned_data['custom3_sonuc']
            istek.custom4_sonuc = form.cleaned_data['custom4_sonuc']
            istek.custom5_sonuc = form.cleaned_data['custom5_sonuc']
            istek.save()

        return super(LabSonucFormView, self).post(request, *args, **kwargs)

    def get_success_url(self):
        pk = self.kwargs['pk']
        istek = LaboratuvarIstek.objects.get(pk=pk)
        return reverse('muayene:detail', kwargs={'pk': istek.muayene_id})

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
