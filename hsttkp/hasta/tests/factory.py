import factory, factory.django
import datetime

from django.contrib.auth.models     import User
from django.utils.text              import slugify

from hasta.models                   import Hasta, Sozlesme

from muayene.models                 import Muayene, Recete, Rapor, Ilac, LaboratuvarIstek

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    email = 'email@example.com'
    username = 'bob'
    password = factory.PostGenerationMethodCall('set_password', 'password')
    is_superuser = True
    is_staff = True
    is_active = True

class HastaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Hasta

    kayit_tarihi = datetime.date.today()
    ad = 'Bob'
    soyad = 'Baz'
    tc_kimlik_no = '12345678901'
    cinsiyet = 'E'
    dogum_tarihi = '1990-12-13'
    meslek = 'Öğretmen'
    es_ad = 'Foo'
    es_meslek = 'Öğretmen'
    cep_telefon = '05456789090'
    ev_telefon = '02324556768'
    is_telefon = '02327898989'
    adres = 'Foo Mh. Bar Sk. Baz Apt. K:2 D:4 Alsancak/İZMİR'
    semt = 'Alsancak'
    eposta = 'bobbaz@email.com'
    sigorta = 'ALLİANZ'
    cocuklar = 'Foo Bar Baz'
    soygecmis = 'SOYGEÇMİŞ'
    ozgecmis = 'ÖZGEÇMİŞ'
    sigara = '10/G'
    alkol = '1 kadeh/g'
    kilo = 70
    boy = 175
    slug = slugify(ad + " " + soyad)

class OldSozlesmeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Sozlesme

    hasta = factory.SubFactory(HastaFactory)
    baslangic_tarihi = '2014-7-4'

class ActiveSozlesmeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Sozlesme

    hasta = factory.SubFactory(HastaFactory)
    baslangic_tarihi = datetime.date.today()

class MuayeneFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Muayene

    hasta = factory.SubFactory(HastaFactory)
    tarih = datetime.date.today()
    kullandigi_ilaclar = 'ilac1 ilac2 ilac3'
    yakinma = 'Genel Sağlık Kontrolü'
    baki = 'BAKI'
    ontani_tani = 'ÖNTANI TANI'
    oneri_gorusler = 'ÖNERİ GÖRÜŞLER'
    ozel_notlar = 'ÖZEL NOTLAR'

class IlacFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ilac

    ad = factory.Sequence(lambda n: "Ilac #%s" % n)
    bilgi = 'İLAÇ BİLGİ'
    kullanim = 'Günde 3'

class ReceteFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Recete

    hasta = factory.SubFactory(HastaFactory)
    muayene = factory.SubFactory(MuayeneFactory)
    tarih = datetime.date.today() 
    ilac1 = factory.SubFactory(IlacFactory)
    ilac1_kullanim = 'İLAÇ 1 KULLANIM'
    ilac1_kutu = 1
    ilac2 = factory.SubFactory(IlacFactory)
    ilac2_kullanim = 'İLAÇ 2 KULLANIM'
    ilac2_kutu = 1
    ilac3 = factory.SubFactory(IlacFactory)
    ilac3_kullanim = 'İLAÇ 3 KULLANIM'
    ilac3_kutu = 1
    ilac4 = factory.SubFactory(IlacFactory)
    ilac4_kullanim = 'İLAÇ 4 KULLANIM'
    ilac4_kutu = 1
    ilac5 = factory.SubFactory(IlacFactory)
    ilac5_kullanim = 'İLAÇ 5 KULLANIM'
    ilac5_kutu = 1

class RaporFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Rapor

    hasta = factory.SubFactory(HastaFactory)
    muayene = factory.SubFactory(MuayeneFactory)
    tarih = datetime.date.today()
    tani = 'Baş ağrısı'
    gun = 1

class LabIstekFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = LaboratuvarIstek

    hasta = factory.SubFactory(HastaFactory)
    muayene = factory.SubFactory(MuayeneFactory)
    tarih = datetime.date.today()
    hemogram = True
    sedim = True
    serum_demir = True
    tdbk = True
