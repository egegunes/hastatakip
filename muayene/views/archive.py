import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.dates import WeekArchiveView, MonthArchiveView, YearArchiveView
from django.views.generic.edit import FormView
from django.views.generic.base import View
from django.template.response import TemplateResponse
from django.http import HttpResponseNotAllowed

from muayene.forms import DateRangeForm
from muayene.models import Muayene


class MuayeneArchiveView(LoginRequiredMixin, FormView):
    form_class = DateRangeForm
    template_name = 'muayene/muayene_archive.html'

    def get(self, request, *args, **kwargs):
        return TemplateResponse(request, self.template_name, {'form': self.form_class()})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            start = form.cleaned_data['start_date']
            end = form.cleaned_data['end_date']
            queryset = Muayene.objects.filter(tarih__gte=start, tarih__lte=end).order_by('-id')
            context = {
                'form': form,
                'start': start,
                'end': end,
                'range_list': queryset
            }
            return TemplateResponse(request, self.template_name, context)


class MuayeneLastCreatedView(LoginRequiredMixin, View):
    template_name = 'muayene/muayene_list.html'

    def get(self, request, *args, **kwargs):
        today = datetime.date.today()
        yesterday = today - datetime.timedelta(days=1)
        queryset = Muayene.objects.filter(tarih__gte=yesterday, tarih__lte=today).order_by('-id')

        return TemplateResponse(request, self.template_name, {'muayene_list': queryset})

    def post(self, request, *args, **kwargs):
        return HttpResponseNotAllowed(['POST'])


class MuayeneWeekArchiveView(LoginRequiredMixin, WeekArchiveView):
    date_field = 'tarih'
    week_format = '%W'
    allow_empty = True
    allow_future = True
    queryset = Muayene.objects.all()

    def post(self, request, *args, **kwargs):
        return HttpResponseNotAllowed(['POST'])


class MuayeneMonthArciveView(LoginRequiredMixin, MonthArchiveView):
    date_field = 'tarih'
    month_format = '%m'
    allow_empty = True
    allow_future = True
    queryset = Muayene.objects.all()

    def post(self, request, *args, **kwargs):
        return HttpResponseNotAllowed(['POST'])


class MuayeneYearArchiveView(LoginRequiredMixin, YearArchiveView):
    date_field = 'tarih'
    year_format = '%Y'
    allow_empty = True
    allow_future = True
    make_object_list = True
    queryset = Muayene.objects.all()

    def post(self, request, *args, **kwargs):
        return HttpResponseNotAllowed(['POST'])
