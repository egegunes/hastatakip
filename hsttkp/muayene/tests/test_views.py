import datetime 
import logging
import json

from unittest.mock              import patch, MagicMock

from unidecode                  import unidecode

from django.core.urlresolvers   import reverse
from django.test                import TestCase, RequestFactory

from .factory                   import *

from muayene.views              import *

# Disable factory_boy's ugly and needless logs!
logging.getLogger("factory").setLevel(logging.WARN)

class BaseTestCase(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.factory = RequestFactory()
        self.hasta = HastaFactory()
        self.muayene = MuayeneFactory(hasta=self.hasta)

class MuayeneArchiveViewTestCase(BaseTestCase):
    def test_get(self):
        request = self.factory.get(reverse('muayene:archive-custom'))
        request.user = self.user

        response = archive.MuayeneArchiveView.as_view()(request)

        self.assertEqual(response.status_code, 200)

        self.assertTrue('form' in response.context_data)

        self.assertTemplateUsed('muayene/muayene_archive.html')

    def test_post(self):
        data = {'start_date': str(datetime.date.today() - datetime.timedelta(days=2)), 'end_date': str(datetime.date.today())}

        request = self.factory.post(reverse('muayene:archive-custom'), data)
        request.user = self.user

        response = archive.MuayeneArchiveView.as_view()(request)

        self.assertEqual(response.status_code, 200)
        
        self.assertTrue('form' in response.context_data)
        self.assertTrue('start' in response.context_data)
        self.assertTrue('end' in response.context_data)
        self.assertTrue('range_list' in response.context_data)
        self.assertEqual(response.context_data['range_list'].count(), 1)

        self.assertTemplateUsed('muayene/muayene_archive.html')

class MuayeneLastCreatedViewTestCase(BaseTestCase):
    def test_get(self):
        request = self.factory.get(reverse('muayene:archive-last'))
        request.user = self.user

        response = archive.MuayeneLastCreatedView.as_view()(request)

        self.assertEqual(response.status_code, 200)

        self.assertTrue('muayene_list' in response.context_data)
        self.assertEqual(response.context_data['muayene_list'].count(), 1)

        self.assertTemplateUsed('muayene/muayene_list.html')

    def test_post(self):
        data = {}

        request = self.factory.post(reverse('muayene:archive-last'), data)
        request.user = self.user

        response = archive.MuayeneLastCreatedView.as_view()(request)

        self.assertEqual(response.status_code, 405)

class MuayeneWeekArchiveViewTestCase(BaseTestCase):
    def test_get(self):
        kwargs = {'year': str(datetime.date.today().year), 'week': str(datetime.date.today().isocalendar()[1])}

        request = self.factory.get(reverse('muayene:archive-week', kwargs=kwargs))
        request.user = self.user

        response = archive.MuayeneWeekArchiveView.as_view()(request, **kwargs)

        self.assertEqual(response.status_code, 200)

        self.assertTrue('object_list' in response.context_data)
        self.assertEqual(response.context_data['object_list'].count(), 1)

        self.assertTemplateUsed('muayene/muayene_archive_week.html')

    def test_post(self):
        kwargs = {'year': str(datetime.date.today().year), 'week': str(datetime.date.today().isocalendar()[1])}
        data = {}

        request = self.factory.post(reverse('muayene:archive-week', kwargs=kwargs), data)
        request.user = self.user

        response = archive.MuayeneWeekArchiveView.as_view()(request, **kwargs)

        self.assertEqual(response.status_code, 405)

class MuayeneMonthArciveViewTestCase(BaseTestCase):
    def test_get(self):
        kwargs = {'year': str(datetime.date.today().year), 'month': str(datetime.date.today().month)}

        request = self.factory.get(reverse('muayene:archive-month', kwargs=kwargs))
        request.user = self.user

        response = archive.MuayeneMonthArciveView.as_view()(request, **kwargs)

        self.assertEqual(response.status_code, 200)

        self.assertTrue('object_list' in response.context_data)
        self.assertEqual(response.context_data['object_list'].count(), 1)

        self.assertTemplateUsed('muayene/muayene_archive_month.html')

    def test_post(self):
        kwargs = {'year': str(datetime.date.today().year), 'month': str(datetime.date.today().month)}
        data = {}

        request = self.factory.post(reverse('muayene:archive-month', kwargs=kwargs), data)
        request.user = self.user

        response = archive.MuayeneMonthArciveView.as_view()(request, **kwargs)

        self.assertEqual(response.status_code, 405)

class MuayeneYearArchiveViewTestCase(BaseTestCase):
    def test_get(self):
        kwargs = {'year': str(datetime.date.today().year)}

        request = self.factory.get(reverse('muayene:archive-year', kwargs=kwargs))
        request.user = self.user

        response = archive.MuayeneYearArchiveView.as_view()(request, **kwargs)

        self.assertEqual(response.status_code, 200)

        self.assertTrue('object_list' in response.context_data)
        self.assertEqual(response.context_data['object_list'].count(), 1)

        self.assertTemplateUsed('muayene/muayene_archive_year.html')

    def test_post(self):
        kwargs = {'year': str(datetime.date.today().year)}
        data = {}

        request = self.factory.post(reverse('muayene:archive-year', kwargs=kwargs), data)
        request.user = self.user

        response = archive.MuayeneYearArchiveView.as_view()(request, **kwargs)

        self.assertEqual(response.status_code, 405)

class MuayeneBaseViewTestCase(BaseTestCase):
    def test_get(self):
        kwargs = {'pk': str(self.muayene.pk)}

        request = self.factory.get(reverse('muayene:detail', kwargs=kwargs))
        request.user = self.user

        ReceteFactory(hasta=self.hasta, muayene=self.muayene)
        RaporFactory(hasta=self.hasta, muayene=self.muayene)
        LabIstekFactory(hasta=self.hasta, muayene=self.muayene)

        response = base.MuayeneBaseView.as_view()(request, **kwargs)

        self.assertEqual(response.status_code, 200)

        self.assertTrue('muayene' in response.context_data)
        self.assertTrue('recete_list' in response.context_data)
        self.assertEqual(response.context_data['recete_list'].count(), 1)
        self.assertTrue('recete_form' in response.context_data)
        self.assertTrue('rapor_list' in response.context_data)
        self.assertEqual(response.context_data['rapor_list'].count(), 1)
        self.assertTrue('rapor_form' in response.context_data)
        self.assertTrue('lab_list' in response.context_data)
        self.assertEqual(response.context_data['lab_list'].count(), 1)
        self.assertTrue('lab_form' in response.context_data)
        self.assertTrue('file_list' in response.context_data)
        self.assertTrue('file_form' in response.context_data)

        self.assertTemplateUsed('muayene/muayene_detail.html')

class MuayeneCreateViewTestCase(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.factory = RequestFactory()
        self.hasta = HastaFactory()

    def test_get(self):
        request = self.factory.get(reverse('muayene:create'))
        request.user = self.user

        response = create.MuayeneCreateView.as_view()(request)

        self.assertEqual(response.status_code, 200)

        self.assertTrue('form' in response.context_data)

        self.assertTemplateUsed('muayene/muayene_form.html')

    def test_get_with_kwargs(self):
        kwargs = {'slug': self.hasta.slug}
        
        request = self.factory.get(reverse('hasta:muayene-create', kwargs=kwargs))
        request.user = self.user

        response = create.MuayeneCreateView.as_view()(request, **kwargs)

        self.assertEqual(response.status_code, 200)

        self.assertTrue('form' in response.context_data)
        self.assertEqual(response.context_data['form']['hasta'].initial, self.hasta.pk)

        self.assertTemplateUsed('muayene/muayene_form.html')

    def test_get_with_kwargs_existing_muayene(self):
        muayene = MuayeneFactory(hasta=self.hasta)

        kwargs = {'slug': str(self.hasta.slug)}

        request = self.factory.get(reverse('hasta:muayene-create', kwargs=kwargs))
        request.user = self.user

        response = create.MuayeneCreateView.as_view()(request, **kwargs)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.get('location'), reverse('muayene:detail', kwargs={'pk': muayene.pk}))

    @patch('muayene.models.Muayene.get_absolute_url')
    @patch('muayene.models.Muayene.save')
    def test_post(self, *args):
        data = {
            'hasta': str(self.hasta.pk),
            'tarih': str(datetime.date.today()),
            'kullandigi_ilaclar': 'ilac1 ilac2 ilac3',
            'yakinma': 'Genel Sağlık Kontrolü',
            'baki': 'BAKI',
            'ontani_tani': 'ÖNTANI / TANI',
            'oneri_gorusler': 'ÖNERİ GÖRÜŞLER',
            'ozel_notlar': 'ÖZEL NOTLAR'
        }

        request = self.factory.post(reverse('muayene:create'), data)
        request.user = self.user

        response = create.MuayeneCreateView.as_view()(request)

        self.assertEqual(response.status_code, 302)

        self.assertTrue(Muayene.get_absolute_url.called)
        self.assertEqual(Muayene.get_absolute_url.call_count, 1)

        self.assertTrue(Muayene.save.called)
        self.assertEqual(Muayene.save.call_count, 1)

    @patch('muayene.models.Muayene.get_absolute_url')
    @patch('muayene.models.Muayene.save')
    def test_post_with_kwargs(self, *args):
        data = {
            'hasta': str(self.hasta.pk),
            'tarih': str(datetime.date.today()),
            'kullandigi_ilaclar': 'ilac1 ilac2 ilac3',
            'yakinma': 'Genel Sağlık Kontrolü',
            'baki': 'BAKI',
            'ontani_tani': 'ÖNTANI / TANI',
            'oneri_gorusler': 'ÖNERİ GÖRÜŞLER',
            'ozel_notlar': 'ÖZEL NOTLAR'
        }
        kwargs = {'slug': str(self.hasta.slug)}

        request = self.factory.post(reverse('hasta:muayene-create', kwargs=kwargs), data)
        request.user = self.user

        response = create.MuayeneCreateView.as_view()(request, **kwargs)

        self.assertEqual(response.status_code, 302)

        self.assertTrue(Muayene.get_absolute_url.called)
        self.assertEqual(Muayene.get_absolute_url.call_count, 1)

        self.assertTrue(Muayene.save.called)
        self.assertEqual(Muayene.save.call_count, 1)

    def test_post_with_kwargs_existing_muayene(self):
        data = {
            'hasta': str(self.hasta.pk),
            'tarih': str(datetime.date.today()),
            'kullandigi_ilaclar': 'ilac1 ilac2 ilac3',
            'yakinma': 'Genel Sağlık Kontrolü',
            'baki': 'BAKI',
            'ontani_tani': 'ÖNTANI / TANI',
            'oneri_gorusler': 'ÖNERİ GÖRÜŞLER',
            'ozel_notlar': 'ÖZEL NOTLAR'
        }
        kwargs = {'slug': str(self.hasta.slug)}

        muayene = MuayeneFactory(hasta=self.hasta)

        request = self.factory.post(reverse('hasta:muayene-create', kwargs=kwargs), data)
        request.user = self.user

        response = create.MuayeneCreateView.as_view()(request, **kwargs)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.get('location'), reverse('muayene:detail', kwargs={'pk': muayene.pk}))

    def test_ajax(self):
        alias = MuayeneAliasFactory()
        data = {'action': 'get_long', 'shorthand': str(alias.shorthand)} 

        request = self.factory.post(reverse('muayene:create'), data, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        request.user = self.user

        response = create.MuayeneCreateView.as_view()(request)

        self.assertEqual(response.status_code, 200)
        
        data = json.loads(response.content.decode())
        self.assertTrue('longhand' in data)
        self.assertEqual(data['longhand'], str(alias.longhand))

class IlacCreateViewTestCase(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.factory = RequestFactory()

    def test_get(self):
        request = self.factory.get(reverse('muayene:ilac-create'))
        request.user = self.user

        response = create.IlacCreateView.as_view()(request)

        self.assertEqual(response.status_code, 200)

        self.assertTrue('form' in response.context_data)

        self.assertTemplateUsed('muayene/ilac_form.html')
        
    @patch('muayene.models.Ilac.get_absolute_url')
    @patch('muayene.models.Ilac.save')
    def test_post(self, *args):
        data = {'ad': 'İlaç ad', 'kullanim': 'İlaç kullanım', 'bilgi': 'İlaç bilgi'}

        request = self.factory.post(reverse('muayene:ilac-create'), data)
        request.user = self.user

        response = create.IlacCreateView.as_view()(request)

        self.assertEqual(response.status_code, 302)

        self.assertTrue(Ilac.get_absolute_url.called)
        self.assertEqual(Ilac.get_absolute_url.call_count, 1)

        self.assertTrue(Ilac.save.called)
        self.assertEqual(Ilac.save.call_count, 1)

class MuayeneAliasCreateViewTestCase(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.factory = RequestFactory()

    def test_get(self):
        request = self.factory.get(reverse('muayene:alias-create'))
        request.user = self.user

        response = create.MuayeneAliasCreateView.as_view()(request)

        self.assertEqual(response.status_code, 200)

        self.assertTrue('form' in response.context_data)

        self.assertTemplateUsed('muayene/muayenealias_form.html')

    @patch('muayene.models.MuayeneAlias.get_absolute_url')
    @patch('muayene.models.MuayeneAlias.save')
    def test_post(self, *args):
        data = {'shorthand': 'nsm', 'longhand': 'Normal sistemik muayene.'}

        request = self.factory.post(reverse('muayene:ilac-create'), data)
        request.user = self.user

        response = create.MuayeneAliasCreateView.as_view()(request)

        self.assertEqual(response.status_code, 302)

        self.assertTrue(MuayeneAlias.get_absolute_url.called)
        self.assertEqual(MuayeneAlias.get_absolute_url.call_count, 1)

        self.assertTrue(MuayeneAlias.save.called)
        self.assertEqual(MuayeneAlias.save.call_count, 1)

class IlacListViewTestCase(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.factory = RequestFactory()
        IlacFactory()

    def test_get(self):
        request = self.factory.get(reverse('muayene:ilac-list'))
        request.user = self.user

        response = list.IlacListView.as_view()(request)

        self.assertEqual(response.status_code, 200)

        self.assertTrue('ilac_list' in response.context_data)
        self.assertEqual(response.context_data['ilac_list'].count(), 1)

        self.assertTemplateUsed('muayene/ilac_list.html')

    def test_post(self):
        data = {}

        request = self.factory.post(reverse('muayene:ilac-list'), data)
        request.user = self.user

        response = list.IlacListView.as_view()(request)

        self.assertEqual(response.status_code, 405)

class LastCreatedLabIstekViewTestCase(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.factory = RequestFactory()
        self.hasta = HastaFactory()
        self.muayene = MuayeneFactory(hasta=self.hasta)
        LabIstekFactory(hasta=self.hasta, muayene=self.muayene)

    def test_get(self):
        request = self.factory.get(reverse('muayene:lab-last'))
        request.user = self.user

        response = list.LastCreatedLabIstekView.as_view()(request)

        self.assertEqual(response.status_code, 200)

        self.assertTrue('istek_list' in response.context_data)
        self.assertEqual(response.context_data['istek_list'].count(), 1)

        self.assertTemplateUsed('muayene/laboratuvaristek_list.html')

    def test_post(self):
        data = {}

        request = self.factory.post(reverse('muayene:lab-last'), data)
        request.user = self.user

        response = list.LastCreatedLabIstekView.as_view()(request)

        self.assertEqual(response.status_code, 405)

class MuayeneAliasListViewTestCase(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.factory = RequestFactory()
        MuayeneAliasFactory()

    def test_get(self):
        request = self.factory.get(reverse('muayene:alias-list'))
        request.user = self.user

        response = list.MuayeneAliasListView.as_view()(request)

        self.assertEqual(response.status_code, 200)

        self.assertTrue('alias_list' in response.context_data)
        self.assertEqual(response.context_data['alias_list'].count(), 1)

        self.assertTemplateUsed('muayene/muayenealias_list.html')

    def test_post(self):
        data = {}

        request = self.factory.post(reverse('muayene:alias-list'), data)
        request.user = self.user

        response = list.MuayeneAliasListView.as_view()(request)

        self.assertEqual(response.status_code, 405)

class IlacSearchViewTestCase(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.factory = RequestFactory()
        IlacFactory()

    def test_get(self):
        request = self.factory.get(reverse('muayene:ilac-ara'))
        request.user = self.user

        response = search.IlacSearchView.as_view()(request)

        self.assertEqual(response.status_code, 405)

    def test_post(self):
        data = {'term': 'ilac'}

        request = self.factory.post(reverse('muayene:ilac-ara'), data)
        request.user = self.user

        response = search.IlacSearchView.as_view()(request)

        self.assertEqual(response.status_code, 200)

        self.assertTrue('ilac_list' in response.context_data)
        self.assertEqual(response.context_data['ilac_list'].count(), 1)

        self.assertTemplateUsed('muayene/ilac_list.html')

class MuayeneUpdateViewTestCase(BaseTestCase):
    def test_get(self):
        request = self.factory.get(reverse('muayene:update', kwargs={'pk': str(self.muayene.pk)}))
        request.user = self.user
    
        response = update.MuayeneUpdateView.as_view()(request, pk=self.muayene.pk)

        self.assertEqual(response.status_code, 200)
        
        self.assertTrue('form' in response.context_data)
        self.assertEqual(response.context_data['form']['hasta'].initial, self.muayene.hasta.pk)
        self.assertEqual(response.context_data['form']['kullandigi_ilaclar'].initial, self.muayene.kullandigi_ilaclar)
        self.assertEqual(response.context_data['form']['yakinma'].initial, self.muayene.yakinma)
        self.assertEqual(response.context_data['form']['baki'].initial, self.muayene.baki)
        self.assertEqual(response.context_data['form']['ontani_tani'].initial, self.muayene.ontani_tani)
        self.assertEqual(response.context_data['form']['oneri_gorusler'].initial, self.muayene.oneri_gorusler)
        self.assertEqual(response.context_data['form']['ozel_notlar'].initial, self.muayene.ozel_notlar)

        self.assertTemplateUsed('muayene/muayene_form.html')

    @patch('muayene.models.Muayene.get_absolute_url')
    @patch('muayene.models.Muayene.save')
    def test_post(self, *args):
        data = {
            'hasta': str(self.hasta.pk),
            'tarih': str(datetime.date.today()),
            'kullandigi_ilaclar': 'ilac1 ilac2 ilac3',
            'yakinma': 'Genel Sağlık Kontrolü',
            'baki': 'BAKI',
            'ontani_tani': 'ÖNTANI / TANI',
            'oneri_gorusler': 'ÖNERİ GÖRÜŞLER',
            'ozel_notlar': 'ÖZEL NOTLAR'
        }

        request = self.factory.post(reverse('muayene:update', kwargs={'pk': str(self.muayene.pk)}), data)
        request.user = self.user

        response = update.MuayeneUpdateView.as_view()(request, pk=self.muayene.pk)
        
        self.assertEqual(response.status_code, 302)

        self.assertTrue(Muayene.get_absolute_url.called)
        self.assertEqual(Muayene.get_absolute_url.call_count, 1)

        self.assertTrue(Muayene.save.called)
        self.assertEqual(Muayene.save.call_count, 1)

class RecetePrintViewTestCase(BaseTestCase):
    def test_get(self):
        recete = ReceteFactory(hasta=self.hasta, muayene=self.muayene)
        ad = str(recete.hasta.ad)
        soyad = str(recete.hasta.soyad)
        pk = str(recete.pk)
        tarih = str(recete.tarih)
        filename = unidecode('%s-%s-recete-%s-%s' % (ad, soyad, pk, tarih))

        request = self.factory.get(reverse('muayene:recete-print', kwargs={'pk': recete.pk}))
        request.user = self.user

        response = prints.RecetePrintView.as_view()(request, pk=recete.pk)

        self.assertEqual(response.status_code, 200)

        self.assertTrue(response.has_header('Content-Type'))
        self.assertEqual(response.get('Content-Type'), 'application/pdf')

        self.assertTrue(response.has_header('Content-Disposition'))
        self.assertEqual(response.get('Content-Disposition'), 'filename=%s.pdf' % filename)

    def test_post(self):
        recete = ReceteFactory(hasta=self.hasta, muayene=self.muayene)

        data = {}

        request = self.factory.post(reverse('muayene:recete-print', kwargs={'pk': recete.pk}), data)
        request.user = self.user

        response = prints.RecetePrintView.as_view()(request, pk=recete.pk)

        self.assertEqual(response.status_code, 405)

class RaporPrintViewTestCase(BaseTestCase):
    def test_get(self):
        rapor = RaporFactory(hasta=self.hasta, muayene=self.muayene)
        ad = str(rapor.hasta.ad)
        soyad = str(rapor.hasta.soyad)
        pk = str(rapor.pk)
        tarih = str(rapor.tarih)
        filename = unidecode('%s-%s-rapor-%s-%s' % (ad, soyad, pk, tarih))

        request = self.factory.get(reverse('muayene:rapor-print', kwargs={'pk': rapor.pk}))
        request.user = self.user

        response = prints.RaporPrintView.as_view()(request, pk=rapor.pk)

        self.assertEqual(response.status_code, 200)

        self.assertTrue(response.has_header('Content-Type'))
        self.assertEqual(response.get('Content-Type'), 'application/pdf')

        self.assertTrue(response.has_header('Content-Disposition'))
        self.assertEqual(response.get('Content-Disposition'), 'filename=%s.pdf' % filename)

    def test_post(self):
        rapor = RaporFactory(hasta=self.hasta, muayene=self.muayene)
        
        data = {}

        request = self.factory.post(reverse('muayene:rapor-print', kwargs={'pk': rapor.pk}), data)
        request.user = self.user

        response = prints.RaporPrintView.as_view()(request, pk=rapor.pk)

        self.assertEqual(response.status_code, 405)

class LabIstekPrintViewTestCase(BaseTestCase):
    def test_get(self):
        istek = LabIstekFactory(hasta=self.hasta, muayene=self.muayene)
        ad = str(istek.hasta.ad)
        soyad = str(istek.hasta.soyad)
        pk = str(istek.pk)
        tarih = str(istek.tarih)
        filename = unidecode('%s-%s-istek-%s-%s' % (ad, soyad, pk, tarih))

        request = self.factory.get(reverse('muayene:lab-print', kwargs={'pk': istek.pk}))
        request.user = self.user

        response = prints.LabIstekPrintView.as_view()(request, pk=istek.pk)

        self.assertEqual(response.status_code, 200)

        self.assertTrue(response.has_header('Content-Type'))
        self.assertEqual(response.get('Content-Type'), 'application/pdf')

        self.assertTrue(response.has_header('Content-Disposition'))
        self.assertEqual(response.get('Content-Disposition'), 'filename=%s.pdf' % filename)

    def test_post(self):
        istek = LabIstekFactory(hasta=self.hasta, muayene=self.muayene)

        data = {}

        request = self.factory.post(reverse('muayene:lab-print', kwargs={'pk': istek.pk}), data)
        request.user = self.user

        response = prints.LabIstekPrintView.as_view()(request, pk=istek.pk)

        self.assertEqual(response.status_code, 405)

class TTFPrintViewTestCase(BaseTestCase):
    def test_get(self):
        ad = str(self.muayene.hasta.ad)
        soyad = str(self.muayene.hasta.soyad)
        pk = str(self.muayene.pk)
        tarih = str(self.muayene.tarih)
        filename = unidecode('%s-%s-ttf-%s-%s' % (ad, soyad, pk, tarih))

        request = self.factory.get(reverse('muayene:ttf-print', kwargs={'pk': self.muayene.pk}))
        request.user = self.user

        response = prints.TTFPrintView.as_view()(request, pk=self.muayene.pk)

        self.assertEqual(response.status_code, 200)

        self.assertTrue(response.has_header('Content-Type'))
        self.assertEqual(response.get('Content-Type'), 'application/pdf')

        self.assertTrue(response.has_header('Content-Disposition'))
        self.assertEqual(response.get('Content-Disposition'), 'filename=%s.pdf' % filename)

    def test_post(self):
        data = {} 

        request = self.factory.post(reverse('muayene:ttf-print', kwargs={'pk': self.muayene.pk}), data)
        request.user = self.user

        response = prints.TTFPrintView.as_view()(request, pk=self.muayene.pk)

        self.assertEqual(response.status_code, 405)

class MultiTTFPrintViewTestCase(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.factory = RequestFactory()
        self.hasta = HastaFactory()
        self.muayene1 = MuayeneFactory(hasta=self.hasta, tarih=datetime.date.today())
        self.muayene2 = MuayeneFactory(hasta=self.hasta, tarih=datetime.date.today() - datetime.timedelta(days=1))
        self.muayene3 = MuayeneFactory(hasta=self.hasta, tarih=datetime.date.today() - datetime.timedelta(days=2))

    def test_get(self):
        request = self.factory.get(reverse('muayene:multi-ttf-print'))
        request.user = self.user

        response = prints.MultiTTFPrintView.as_view()(request)

        self.assertEqual(response.status_code, 405)

    def test_post(self):
        start = str(datetime.date.today() - datetime.timedelta(days=2))
        end = str(datetime.date.today())
        data = {'end': end, 'start': start}
        filename = '%s-%s-ttf' % (start, end)

        request = self.factory.post(reverse('muayene:multi-ttf-print'), data)
        request.user = self.user

        response = prints.MultiTTFPrintView.as_view()(request)

        self.assertEqual(response.status_code, 200)

        self.assertTrue(response.has_header('Content-Type'))
        self.assertEqual(response.get('Content-Type'), 'application/pdf')

        self.assertTrue(response.has_header('Content-Disposition'))
        self.assertEqual(response.get('Content-Disposition'), 'filename=%s.pdf' % filename)

class AHSevkPrintViewTestCase(BaseTestCase):
    def test_get(self):
        ad = str(self.muayene.hasta.ad)
        soyad = str(self.muayene.hasta.soyad)
        pk = str(self.muayene.pk)
        tarih = str(self.muayene.tarih)
        filename = unidecode('%s-%s-ahsevk-%s-%s' % (ad, soyad, pk, tarih))

        request = self.factory.get(reverse('muayene:ahsevk', kwargs={'pk': self.muayene.pk}))
        request.user = self.user

        response = prints.AHSevkPrintView.as_view()(request, pk=self.muayene.pk)

        self.assertEqual(response.status_code, 200)

        self.assertTrue(response.has_header('Content-Type'))
        self.assertEqual(response.get('Content-Type'), 'application/pdf')

        self.assertTrue(response.has_header('Content-Disposition'))
        self.assertEqual(response.get('Content-Disposition'), 'filename=%s.pdf' % filename)

    def test_post(self):
        data = {}

        request = self.factory.post(reverse('muayene:ahsevk', kwargs={'pk': self.muayene.pk}), data)
        request.user = self.user

        response = prints.AHSevkPrintView.as_view()(request, pk=self.muayene.pk)

        self.assertEqual(response.status_code, 405)

