import datetime 
import logging

from unittest.mock              import patch, MagicMock

from django.core.urlresolvers   import reverse
from django.test                import TestCase, RequestFactory

from .factory                   import *

from hasta.models               import Hasta, Sozlesme
from hasta.views                import (
                                        HastaCreateView, 
                                        HastaUpdateView, 
                                        HastaDetailView,
                                        HastaDetailBaseView,
                                        HastaLastCreatedView,
                                        HastaListView,
                                        SozlesmeListView,
                                        MuayeneListView,
                                        ReceteListView,
                                        RaporListView,
                                        LabIstekListView,
                                        HastaSearchView
                                        )

# Disable factory_boy's ugly and needless logs!
logging.getLogger("factory").setLevel(logging.WARN)

class HastaCreateViewTestCase(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.factory = RequestFactory()
        self.data = {
            'ad': 'Bob',
            'soyad': 'Baz',
            'tc_kimlik_no': '12345678901',
            'cinsiyet': 'E',
            'dogum_tarihi': '1990-12-13',
            'sigorta': 'ALLİANZ',
            'meslek': 'Öğretmen',
            'es_ad': 'Foo',
            'es_meslek': 'Öğretmen',
            'cep_telefon': '05456789090',
            'ev_telefon': '02324556768',
            'is_telefon': '02327898989',
            'adres': 'Foo Mh. Bar Sk. Baz Apt. K:2 D:4 Alsancak/İZMİR',
            'semt': 'Alsancak',
            'eposta': 'bobbaz@email.com',
            'cocuklar': 'Foo Bar Baz',
            'soygecmis': 'SOYGEÇMİŞ',
            'ozgecmis': 'ÖZGEÇMİŞ',
            'sigara': '10/G',
            'alkol': '1 kadeh/g',
            'kilo': 70,
            'boy': 175
        }

    def test_get(self):
        request = self.factory.get(reverse('hasta:create'))
        request.user = self.user

        response = HastaCreateView.as_view()(request)

        self.assertEqual(response.status_code, 200)

        self.assertTrue('form' in response.context_data)

        self.assertTrue('hasta/hasta_form.html' in response.template_name)

    @patch('hasta.models.Hasta.get_absolute_url')
    @patch('hasta.models.Hasta.save')
    def test_post(self, *args):
        request = self.factory.post(reverse('hasta:create'), self.data)
        request.user = self.user

        response = HastaCreateView.as_view()(request)

        self.assertEqual(response.status_code, 302)

        self.assertTrue(Hasta.get_absolute_url.called)
        self.assertEqual(Hasta.get_absolute_url.call_count, 1)

        self.assertTrue(Hasta.save.called)
        self.assertEqual(Hasta.save.call_count, 1)

class HastaUpdateViewTestCase(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.factory = RequestFactory()
        self.hasta = HastaFactory()
        self.kwargs = {'slug': str(self.hasta.slug)}
        self.data = {
            'ad': 'Bob',
            'soyad': 'Baz',
            'tc_kimlik_no': '12345678901',
            'cinsiyet': 'E',
            'dogum_tarihi': '1990-12-13',
            'sigorta': 'ALLİANZ',
            'meslek': 'Öğretmen',
            'es_ad': 'Foo',
            'es_meslek': 'Öğretmen',
            'cep_telefon': '05456789090',
            'ev_telefon': '02324556768',
            'is_telefon': '02327898989',
            'adres': 'Foo Mh. Bar Sk. Baz Apt. K:2 D:4 Alsancak/İZMİR',
            'semt': 'Alsancak',
            'eposta': 'bobbaz@email.com',
            'cocuklar': 'Foo Bar Baz',
            'soygecmis': 'SOYGEÇMİŞ',
            'ozgecmis': 'ÖZGEÇMİŞ',
            'sigara': '10/G',
            'alkol': '1 kadeh/g',
            'kilo': 70,
            'boy': 175
        }

    def test_get(self):
        request = self.factory.get(reverse('hasta:update', kwargs=self.kwargs))
        request.user = self.user

        response = HastaUpdateView.as_view()(request, **self.kwargs)

        self.assertEqual(response.status_code, 200)

        self.assertTrue('form' in response.context_data)

        self.assertTrue('hasta/hasta_form.html' in response.template_name)

    @patch('hasta.models.Hasta.get_absolute_url')
    @patch('hasta.models.Hasta.save')
    def test_post(self, *args):
        request = self.factory.post(reverse('hasta:update', kwargs=self.kwargs), self.data)
        request.user = self.user

        response = HastaUpdateView.as_view()(request, **self.kwargs)

        self.assertEqual(response.status_code, 302)

        self.assertTrue(Hasta.get_absolute_url.called)
        self.assertEqual(Hasta.get_absolute_url.call_count, 1)

        self.assertTrue(Hasta.save.called)
        self.assertEqual(Hasta.save.call_count, 1)

class HastaDetailViewTestCase(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.factory = RequestFactory()
        self.hasta = HastaFactory()
        self.kwargs = {'slug': str(self.hasta.slug)}

    def test_get(self):
        request = self.factory.get(reverse('hasta:detail', kwargs=self.kwargs))
        request.user = self.user

        muayene=MuayeneFactory(hasta=self.hasta)
        ReceteFactory(hasta=self.hasta, muayene=muayene)
        RaporFactory(hasta=self.hasta, muayene=muayene)
        LabIstekFactory(hasta=self.hasta, muayene=muayene)

        response = HastaDetailBaseView.as_view()(request, slug=self.hasta.slug)

        self.assertEqual(response.status_code, 200)

        self.assertTrue('hasta' in response.context_data)
        self.assertTrue('muayene_list' in response.context_data)
        self.assertGreater(response.context_data['muayene_list'].count(), 0)
        self.assertTrue('recete_list' in response.context_data)
        self.assertGreater(response.context_data['recete_list'].count(), 0)
        self.assertTrue('rapor_list' in response.context_data)
        self.assertGreater(response.context_data['rapor_list'].count(), 0)
        self.assertTrue('lab_list' in response.context_data)
        self.assertGreater(response.context_data['lab_list'].count(), 0)

        self.assertTrue('hasta/hasta_detail.html' in response.template_name)

    def test_post(self):
        request = self.factory.post(reverse('hasta:detail', kwargs=self.kwargs), {'sozlesme': 'Onayla'})
        request.user = self.user

        response = HastaDetailBaseView.as_view()(request, slug=self.hasta.slug)

        self.assertEqual(response.status_code, 302)

class HastaListViewTestCase(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.factory = RequestFactory()

    def test_get(self):
        request = self.factory.get(reverse('hasta:list'))
        request.user = self.user

        response = HastaListView.as_view()(request)

        self.assertEqual(response.status_code, 200)

        self.assertTrue('hasta_list' in response.context_data)

        self.assertTrue('hasta/hasta_list.html' in response.template_name)

    def test_post(self):
        data = {}

        request = self.factory.post(reverse('hasta:list'), data)
        request.user = self.user

        response = HastaListView.as_view()(request)

        self.assertEqual(response.status_code, 405)

class HastaLastCreatedViewTestCase(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.factory = RequestFactory()
        self.hasta = HastaFactory()

    def test_get(self):
        request = self.factory.get(reverse('hasta:created-last'))
        request.user = self.user

        response = HastaLastCreatedView.as_view()(request)

        self.assertEqual(response.status_code, 200)

        self.assertTrue('hasta_list' in response.context_data)
        self.assertGreater(response.context_data['hasta_list'].count(), 0)

        self.assertTrue('hasta/hasta_list.html' in response.template_name)

    def test_post(self):
        data = {}

        request = self.factory.post(reverse('hasta:created-last'), data)
        request.user = self.user

        response = HastaLastCreatedView.as_view()(request)

        self.assertEqual(response.status_code, 405)

class SozlesmeListViewTestCase(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.factory = RequestFactory()
        self.sozlesme = ActiveSozlesmeFactory()

    def test_get(self):
        request = self.factory.get(reverse('hasta:sozlesme-list'))
        request.user = self.user

        response = SozlesmeListView.as_view()(request)

        self.assertEqual(response.status_code, 200)

        self.assertTrue('sozlesme_list' in response.context_data)
        self.assertGreater(response.context_data['sozlesme_list'].count(), 0)

        self.assertTrue('hasta/sozlesme_list.html' in response.template_name)

    def test_post(self):
        data = {}

        request = self.factory.post(reverse('hasta:sozlesme-list'), data)
        request.user = self.user

        response = SozlesmeListView.as_view()(request)

        self.assertEqual(response.status_code, 405)

class MuayeneListViewTestCase(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.factory = RequestFactory()
        self.hasta = HastaFactory()
        self.kwargs = {'slug': self.hasta.slug}
        MuayeneFactory(hasta=self.hasta)

    def test_get(self):
        request = self.factory.get(reverse('hasta:muayene-list', kwargs=self.kwargs))
        request.user = self.user

        response = MuayeneListView.as_view()(request, **self.kwargs)

        self.assertEqual(response.status_code, 200)

        self.assertTrue('muayene_list' in response.context_data)
        self.assertEqual(response.context_data['muayene_list'].count(), 1)

        self.assertTrue('muayene/muayene_list.html' in response.template_name)

    def test_post(self):
        data = {}

        request = self.factory.post(reverse('hasta:muayene-list', kwargs=self.kwargs), data)
        request.user = self.user

        response = MuayeneListView.as_view()(request)

        self.assertEqual(response.status_code, 405)

class ReceteListViewTestCase(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.factory = RequestFactory()
        self.hasta = HastaFactory()
        self.kwargs = {'slug': self.hasta.slug}
        self.muayene = MuayeneFactory(hasta=self.hasta)
        ReceteFactory(hasta=self.hasta, muayene=self.muayene)

    def test_get(self):
        request = self.factory.get(reverse('hasta:recete-list', kwargs=self.kwargs))
        request.user = self.user

        response = ReceteListView.as_view()(request, **self.kwargs)

        self.assertEqual(response.status_code, 200)

        self.assertTrue('recete_list' in response.context_data)
        self.assertEqual(response.context_data['recete_list'].count(), 1)

        self.assertTrue('muayene/recete_list.html' in response.template_name)

    def test_post(self):
        data = {}

        request = self.factory.post(reverse('hasta:recete-list', kwargs=self.kwargs), data)
        request.user = self.user

        response = ReceteListView.as_view()(request)

        self.assertEqual(response.status_code, 405)

class RaporListViewTestCase(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.factory = RequestFactory()
        self.hasta = HastaFactory()
        self.kwargs = {'slug': self.hasta.slug}
        self.muayene = MuayeneFactory(hasta=self.hasta)
        RaporFactory(hasta=self.hasta, muayene=self.muayene)

    def test_get(self):
        request = self.factory.get(reverse('hasta:rapor-list', kwargs=self.kwargs))
        request.user = self.user

        response = RaporListView.as_view()(request, **self.kwargs)

        self.assertEqual(response.status_code, 200)

        self.assertTrue('rapor_list' in response.context_data)
        self.assertEqual(response.context_data['rapor_list'].count(), 1)

        self.assertTrue('muayene/rapor_list.html' in response.template_name)

    def test_post(self):
        data = {}

        request = self.factory.post(reverse('hasta:rapor-list', kwargs=self.kwargs), data)
        request.user = self.user

        response = RaporListView.as_view()(request)

        self.assertEqual(response.status_code, 405)

class LabIstekListViewTestCase(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.factory = RequestFactory()
        self.hasta = HastaFactory()
        self.kwargs = {'slug': self.hasta.slug}
        self.muayene = MuayeneFactory(hasta=self.hasta)
        LabIstekFactory(hasta=self.hasta, muayene=self.muayene)

    def test_get(self):
        request = self.factory.get(reverse('hasta:istek-list', kwargs=self.kwargs))
        request.user = self.user

        response = LabIstekListView.as_view()(request, **self.kwargs)

        self.assertEqual(response.status_code, 200)

        self.assertTrue('istek_list' in response.context_data)
        self.assertEqual(response.context_data['istek_list'].count(), 1)

        self.assertTrue('muayene/laboratuvaristek_list.html' in response.template_name)

    def test_post(self):
        data = {}

        request = self.factory.post(reverse('hasta:istek-list', kwargs=self.kwargs), data)
        request.user = self.user

        response = LabIstekListView.as_view()(request)

        self.assertEqual(response.status_code, 405)

class HastaSearchViewTestCase(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.factory = RequestFactory()
        self.hasta = HastaFactory()

    def test_get(self):
        request = self.factory.get(reverse('hasta:search'))
        request.user = self.user

        response = HastaSearchView.as_view()(request)

        self.assertEqual(response.status_code, 405)

    def test_post(self):
        request = self.factory.post(reverse('hasta:search'), {'term': 'Bob Baz'})
        request.user = self.user

        response = HastaSearchView.as_view()(request)

        self.assertEqual(response.status_code, 200)

        self.assertTrue('hasta_list' in response.context_data)
        self.assertEqual(response.context_data['hasta_list'].count(), 1)

        self.assertTrue('hasta/hasta_list.html' in response.template_name)
