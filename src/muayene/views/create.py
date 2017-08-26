import datetime
import json
import logging

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect

from muayene.models import Muayene, Ilac, Recete, MuayeneAlias, ReceteIlac
from muayene.forms import MuayeneCreateForm, ReceteIlacForm

from hasta.models import Hasta

logger = logging.getLogger(__name__)


class MuayeneCreateView(LoginRequiredMixin, CreateView):
    """
    CreateView for muayene object.

    If redirecting from a HastaDetailView, Hasta field take that Hasta object initially.
    Then checks for muayene object is the only muayene entry in relation with
    redirected hasta object for today. Every hasta object can hold one and only
    one muayene entry for each day. If an entry already created today, redirect
    that object's detail page instead of muayene_form.

    If accessed with /muayene/yeni url and post some data, it controls that
    again. If finds an entry, redirects to that object's detail page instead of
    creating new entry.

    URL: /muayene/yeni
    """

    login_url = '/login/'
    model = Muayene
    form_class = MuayeneCreateForm

    def get(self, request, *args, **kwargs):
        if 'slug' in self.kwargs:
            slug = self.kwargs['slug']
            hasta = Hasta.objects.get(slug=slug)
            qs = Muayene.objects.filter(hasta=hasta)
            today = datetime.date.today()

            if qs.filter(tarih=today).count() > 0:
                muayene = Muayene.objects.get(hasta=hasta, tarih=today)
                return HttpResponseRedirect(reverse('muayene:detail', kwargs={'pk': muayene.pk}))
            else:
                return super(MuayeneCreateView, self).get(request, *args, **kwargs)

        else:
            return super(MuayeneCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            return self.ajax(request)

        hasta_id = request.POST.get('hasta', '')
        hasta = Hasta.objects.get(pk=hasta_id)
        qs = Muayene.objects.filter(hasta=hasta)
        today = datetime.date.today()

        if qs.filter(tarih=today).count() > 0:
            muayene = Muayene.objects.get(hasta=hasta, tarih=today)
            return HttpResponseRedirect(reverse('muayene:detail', kwargs={'pk': muayene.pk}))
        else:
            return super(MuayeneCreateView, self).post(request, *args, **kwargs)

    def ajax(self, request):
        response_dict = {
            'success': True,
        }

        data = request.POST.get('shorthand', '')
        terms = data.split()
        response = []

        for term in terms:
            response.append(MuayeneAlias.objects.get(shorthand=term).longhand)

        response_str = ' '.join(response)

        response_dict = {
            'longhand': response_str
        }

        return HttpResponse(json.dumps(response_dict))

    def get_initial(self, **kwargs):
        if 'slug' in self.kwargs:
            slug = self.kwargs['slug']
            hasta = Hasta.objects.get(slug=slug)
            return {'hasta': hasta.pk}
        else:
            return {}


class ReceteCreateView(CreateView):
    model = Recete
    form_class = ReceteIlacForm

    def post(self, request, *args, **kwargs):
        muayene = Muayene.objects.get(pk=kwargs.get('pk'))
        ilaclar = json.loads(request.POST.get('ilaclar'))

        recete = Recete.objects.create(hasta=muayene.hasta, muayene=muayene)

        for ilac in ilaclar:
            form = self.form_class(ilac)
            if form.is_valid():
                recete_ilac = ReceteIlac.objects.create(
                    ilac=Ilac.objects.get(pk=ilac['ilac']),
                    kullanim=ilac['kullanim'],
                    kutu=ilac['kutu']
                )
                recete.ilaclar.add(recete_ilac)
            else:
                logger.error('{} is not valid'.format(ilac))

        return HttpResponse(status=201)
