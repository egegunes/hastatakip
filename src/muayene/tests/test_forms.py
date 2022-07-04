import datetime

from django.test import TestCase

from .factory import *

from muayene.forms import *


class MuayeneCreateFormTestCase(TestCase):
    def test_empty(self):
        data = {}

        form = MuayeneCreateForm(data)

        self.assertFalse(form.is_valid())

    def test_invalid(self):
        data = {
            "tarih": str(datetime.date.today()),
            "kullandigi_ilaclar": "ilac1 ilac2 ilac3",
            "yakinma": "Genel Sağlık Kontrolü",
            "baki": "BAKI",
            "ontani_tani": "ÖNTANI / TANI",
            "oneri_gorusler": "ÖNERİ GÖRÜŞLER",
            "ozel_notlar": "ÖZEL NOTLAR",
        }

        form = MuayeneCreateForm(data)

        self.assertFalse(form.is_valid())

    def test_valid(self):
        hasta = HastaFactory()

        data = {
            "hasta": str(hasta.pk),
            "tarih": str(datetime.date.today()),
            "kullandigi_ilaclar": "ilac1 ilac2 ilac3",
            "yakinma": "Genel Sağlık Kontrolü",
            "baki": "BAKI",
            "ontani_tani": "ÖNTANI / TANI",
            "oneri_gorusler": "ÖNERİ GÖRÜŞLER",
            "ozel_notlar": "ÖZEL NOTLAR",
        }

        form = MuayeneCreateForm(data)

        self.assertTrue(form.is_valid())


class IlacCreateFormTestCase(TestCase):
    def test_empty(self):
        data = {}

        form = IlacCreateForm(data)

        self.assertFalse(form.is_valid())

    def test_invalid(self):
        data = {"ad": "İlaç", "bilgi": "İlaç bilgi"}

        form = IlacCreateForm(data)

        self.assertFalse(form.is_valid())

    def test_valid(self):
        data = {"ad": "İlaç", "kullanim": "İlaç kullanım", "bilgi": "Bilgi"}

        form = IlacCreateForm(data)

        self.assertTrue(form.is_valid())


class ReceteCreateFormTestCase(TestCase):
    def setUp(self):
        self.ilac1 = IlacFactory()
        self.ilac2 = IlacFactory()
        self.ilac3 = IlacFactory()
        self.ilac4 = IlacFactory()
        self.ilac5 = IlacFactory()

    def test_empty(self):
        data = {}

        form = ReceteCreateForm(data)

        self.assertFalse(form.is_valid())

    def test_invalid(self):
        data = {
            "ilac1": str(self.ilac1.pk),
            "ilac1_kutu": 1,
            "ilac2": str(self.ilac2.pk),
            "ilac2_kullanim": str(self.ilac2.kullanim),
            "ilac2_kutu": 1,
            "ilac3": str(self.ilac3.pk),
            "ilac3_kullanim": str(self.ilac3.kullanim),
            "ilac3_kutu": 1,
            "ilac4": str(self.ilac4.pk),
            "ilac4_kullanim": str(self.ilac4.kullanim),
            "ilac4_kutu": 1,
            "ilac5": str(self.ilac5.pk),
            "ilac5_kullanim": str(self.ilac5.kullanim),
            "ilac5_kutu": 1,
        }

        form = ReceteCreateForm(data)

        self.assertFalse(form.is_valid())

    def test_valid(self):
        data = {
            "ilac1": str(self.ilac1.pk),
            "ilac1_kullanim": str(self.ilac1.kullanim),
            "ilac1_kutu": 1,
            "ilac2": str(self.ilac2.pk),
            "ilac2_kullanim": str(self.ilac2.kullanim),
            "ilac2_kutu": 1,
            "ilac3": str(self.ilac3.pk),
            "ilac3_kullanim": str(self.ilac3.kullanim),
            "ilac3_kutu": 1,
            "ilac4": str(self.ilac4.pk),
            "ilac4_kullanim": str(self.ilac4.kullanim),
            "ilac4_kutu": 1,
            "ilac5": str(self.ilac5.pk),
            "ilac5_kullanim": str(self.ilac5.kullanim),
            "ilac5_kutu": 1,
        }

        form = ReceteCreateForm(data)

        self.assertTrue(form.is_valid())


class RaporCreateFormTestCase(TestCase):
    def test_empty(self):
        data = {}

        form = RaporCreateForm(data)

        self.assertFalse(form.is_valid())

    def test_invalid(self):
        data = {"gun": 2}

        form = RaporCreateForm(data)

        self.assertFalse(form.is_valid())

    def test_valid(self):
        data = {"tani": "TANI", "gun": 2}

        form = RaporCreateForm(data)

        self.assertTrue(form.is_valid())


class LaboratuvarIstekFormTestCase(TestCase):
    def test_empty(self):
        data = {}

        form = LaboratuvarIstekForm(data)

        self.assertTrue(form.is_valid())

    def test_valid(self):
        data = {
            "hemogram": True,
            "hemogram_sonuc": "HEMOGRAM SONUÇ",
            "sedim": True,
            "sedim_sonuc": "SEDİM SONUÇ",
        }

        form = LaboratuvarIstekForm(data)

        self.assertTrue(form.is_valid())


class DateRangeFormTestCase(TestCase):
    def test_empty(self):
        data = {}

        form = DateRangeForm(data)

        self.assertFalse(form.is_valid())

    def test_invalid(self):
        data = {"start_date": "9-8-2016", "end_date": "10-8-2016"}

        form = DateRangeForm(data)

        self.assertFalse(form.is_valid())

    def test_valid(self):
        data = {"start_date": "2016-9-18", "end_date": "2016-9-25"}

        form = DateRangeForm(data)

        self.assertTrue(form.is_valid())


class MuayeneAliasCreateFormTestCase(TestCase):
    def test_empty(self):
        data = {}

        form = MuayeneAliasCreateForm(data)

        self.assertFalse(form.is_valid())

    def test_invalid(self):
        data = {
            "shorthand": True,
        }

        form = MuayeneAliasCreateForm(data)

        self.assertFalse(form.is_valid())

    def test_valid(self):
        data = {"shorthand": "nsm", "longhand": "Normal Sistemik Muayene."}

        form = MuayeneAliasCreateForm(data)

        self.assertTrue(form.is_valid())
