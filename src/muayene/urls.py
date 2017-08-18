# -*- coding: utf-8 -*-

from django.conf.urls   import url

from muayene import views

app_name = 'muayene'
urlpatterns = [
    url(
        r'^$',
        views.MuayeneCreateView.as_view(),
        name='index'
    ),
    url(
        r'^(?P<pk>[0-9]+)/$',
        views.MuayeneBaseView.as_view(),
        name='detail'
    ),        
    url(
        r'^(?P<pk>[0-9]+)/duzenle/$',
        views.MuayeneUpdateView.as_view(),
        name='update'
    ),        
    url(
        r'^(?P<pk>[0-9]+)/ttf/$',
        views.TTFPrintView.as_view(),
        name='ttf-print'
    ),        
    url(
        r'^ttf/multi$',
        views.MultiTTFPrintView.as_view(),
        name='multi-ttf-print'
    ),        
    url(
        r'^list-print/$',
        views.ListPrintView.as_view(),
        name='list-print'
    ),
    url(
        r'^(?P<pk>[0-9]+)/ahsevk/$',
        views.AHSevkPrintView.as_view(),
        name='ahsevk'
    ),
    url(
        r'^yeni/$',
        views.MuayeneCreateView.as_view(),
        name='create'
    ),
    url(
        r'^arsiv/$',
        views.MuayeneArchiveView.as_view(),
        name='archive-custom'
    ),
    url(
        r'^arsiv/(?P<year>[0-9]{4})/hafta/(?P<week>[0-9]+)/$',
        views.MuayeneWeekArchiveView.as_view(),
        name = 'archive-week'
    ),
    url(
        r'^arsiv/(?P<year>[0-9]{4})/(?P<month>[0-9]+)/$',
        views.MuayeneMonthArciveView.as_view(),
        name = 'archive-month'
    ),
    url(
        r'^arsiv/(?P<year>[0-9]{4})/$',
        views.MuayeneYearArchiveView.as_view(),
        name = 'archive-year'
    ),
    url(
        r'^list/son/$',
        views.MuayeneLastCreatedView.as_view(),
        name='archive-last'
    ),
    url(
        r'^list/lab/son/$',
        views.LastCreatedLabIstekView.as_view(),
        name='lab-last'
    ),
    url(
        r'^recete/(?P<pk>[0-9]+)/print/$',
        views.RecetePrintView.as_view(),
        name='recete-print'
    ),
    url(
        r'^rapor/(?P<pk>[0-9]+)/print/$',
        views.RaporPrintView.as_view(),
        name='rapor-print'
    ),
    url(
        r'^lab/(?P<pk>[0-9]+)/print/$',
        views.LabIstekPrintView.as_view(),
        name='lab-print'
    ),
    url(
        r'^lab/(?P<pk>[0-9]+)/sonuc/$',
        views.LabSonucFormView.as_view(),
        name='lab-sonuc'
    ),
]
