from django.conf.urls import url

from randevu import views


app_name = 'randevu'
urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$', views.RandevuDetailView.as_view(), name='detail'),
    url(r'ekle/$', views.RandevuCreateView.as_view(), name='create'),
    url(r'list/$', views.RandevuListView.as_view(), name='list'),
    url(r'^(?P<pk>[0-9]+)/guncelle/$', views.RandevuUpdateView.as_view(), name='update'),
    url(r'^(?P<pk>[0-9]+)/iptal/$', views.RandevuCancelView.as_view(), name='cancel'),
    url(r'^(?P<year>[0-9]{4})/hafta/(?P<week>[0-9]+)/$', views.RandevuWeekArchiveView.as_view(), name='week-archive'),
    url(r'^(?P<year>[0-9]{4})/(?P<month>[0-9]+)/(?P<day>[0-9]+)/$', views.RandevuDayArchiveView.as_view(), name='day-archive'),
    url(r'^bugun/$', views.RandevuTodayArchiveView.as_view(), name='today-archive')
]
