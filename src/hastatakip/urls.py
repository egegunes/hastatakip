# -*- coding: utf-8 -*-

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static

from hastatakip import views

urlpatterns = [
    url(r'^$', views.MainIndexView.as_view(), name="index"),
    url(r'^login/', views.LoginView.as_view(), name='login'),
    url(r'^accounts/login/', views.LoginView.as_view(), name='accounts-login'),
    url(r'^logout/', views.LogoutView.as_view(), name='logout'),
    url(r'^hasta/', include('hasta.urls')),
    url(r'^muayene/', include('muayene.urls')),
    url(r'^randevu/', include('randevu.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
