from django.test import TestCase

from hasta.forms import HastaCreateForm


class HastaCreateFormTestCase(TestCase):
    def test_empty(self):
        data = {}
        form = HastaCreateForm(data)

        self.assertFalse(form.is_valid())

    def test_invalid(self):
        data = {
            "ad": "Bob",
            "tc_kimlik_no": "12345678901",
            "cinsiyet": "E",
            "sigorta": "ALLİANZ",
            "meslek": "Öğretmen",
            "es_ad": "Foo",
            "es_meslek": "Öğretmen",
            "cep_telefon": "05456789090",
            "ev_telefon": "02324556768",
            "is_telefon": "02327898989",
            "adres": "Foo Mh. Bar Sk. Baz Apt. K:2 D:4 Alsancak/İZMİR",
            "semt": "Alsancak",
            "eposta": "bobbaz@email.com",
            "cocuklar": "Foo Bar Baz",
            "soygecmis": "SOYGEÇMİŞ",
            "ozgecmis": "ÖZGEÇMİŞ",
            "sigara": "10/G",
            "alkol": "1 kadeh/g",
            "kilo": 70,
            "boy": 175,
        }
        form = HastaCreateForm(data)

        self.assertFalse(form.is_valid())

    def test_valid(self):
        data = {
            "ad": "Bob",
            "soyad": "Baz",
            "tc_kimlik_no": "12345678901",
            "cinsiyet": "E",
            "dogum_tarihi": "1990-12-13",
            "sigorta": "ALLİANZ",
            "meslek": "Öğretmen",
            "es_ad": "Foo",
            "es_meslek": "Öğretmen",
            "cep_telefon": "05456789090",
            "ev_telefon": "02324556768",
            "is_telefon": "02327898989",
            "adres": "Foo Mh. Bar Sk. Baz Apt. K:2 D:4 Alsancak/İZMİR",
            "semt": "Alsancak",
            "eposta": "bobbaz@email.com",
            "cocuklar": "Foo Bar Baz",
            "soygecmis": "SOYGEÇMİŞ",
            "ozgecmis": "ÖZGEÇMİŞ",
            "sigara": "10/G",
            "alkol": "1 kadeh/g",
            "kilo": 70,
            "boy": 175,
        }
        form = HastaCreateForm(data)

        self.assertTrue(form.is_valid())
