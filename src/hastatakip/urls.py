# -*- coding: utf-8 -*-

"""hastatakip URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static

from hastatakip import views

urlpatterns = (
    [
        url(r"^admin/", admin.site.urls),
        url(r"^$", views.MainIndexView.as_view(), name="index"),
        url(r"^login/", views.LoginView.as_view(), name="login"),
        url(r"^accounts/login/", views.LoginView.as_view(), name="accounts-login"),
        url(r"^logout/", views.LogoutView.as_view(), name="logout"),
        url(r"^hasta/", include("hasta.urls")),
        url(r"^muayene/", include("muayene.urls")),
        url(r"^randevu/", include("randevu.urls")),
        url(
            r"^api/autocomplete/hasta/",
            views.HastaAutocomplete.as_view(),
            name="hastaAutocomplete",
        ),
        url(
            r"^api/autocomplete/ilac/",
            views.IlacAutocomplete.as_view(),
            name="IlacAutocomplete",
        ),
    ]
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)
