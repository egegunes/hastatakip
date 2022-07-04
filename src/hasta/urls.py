# -*- coding: utf-8 -*-

from django.views.decorators.cache import cache_page
from django.conf.urls import url

from hasta import views
from muayene.views import create

app_name = "hasta"
urlpatterns = [
    url(r"^list/$", cache_page(60 * 5)(views.HastaListView.as_view()), name="list"),
    url(r"^ara/$", views.HastaSearchView.as_view(), name="search"),
    url(r"^list/son/$", views.HastaLastCreatedView.as_view(), name="created-last"),
    url(r"^list/sozlesme/$", views.SozlesmeListView.as_view(), name="sozlesme-list"),
    url(r"^ekle/$", views.HastaCreateView.as_view(), name="create"),
    url(r"^(?P<slug>[\w-]+)/duzenle/$", views.HastaUpdateView.as_view(), name="update"),
    url(r"^(?P<slug>[\w-]+)/$", views.HastaDetailBaseView.as_view(), name="detail"),
    url(
        r"^(?P<slug>[\w-]+)/muayene/$",
        create.MuayeneCreateView.as_view(),
        name="muayene-create",
    ),
    url(
        r"^(?P<slug>[\w-]+)/muayeneler/$",
        views.MuayeneListView.as_view(),
        name="muayene-list",
    ),
    url(
        r"^(?P<slug>[\w-]+)/receteler/$",
        views.ReceteListView.as_view(),
        name="recete-list",
    ),
    url(
        r"^(?P<slug>[\w-]+)/raporlar/$",
        views.RaporListView.as_view(),
        name="rapor-list",
    ),
    url(
        r"^(?P<slug>[\w-]+)/istekler/$",
        views.LabIstekListView.as_view(),
        name="istek-list",
    ),
    url(
        r"^(?P<slug>[\w-]+)/dosyalar/$",
        views.DosyaListView.as_view(),
        name="dosya-list",
    ),
]
