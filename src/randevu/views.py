from datetime import datetime, timedelta

from django.shortcuts import render
from django.views import generic, View
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, HttpResponseNotAllowed
from django.urls import reverse

from randevu.models import Randevu
from randevu.forms import RandevuCreateForm


class RandevuCreateView(generic.CreateView):
    model = Randevu
    form_class = RandevuCreateForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            randevu = Randevu.objects.create(state=Randevu.STATE_OPEN, **form.cleaned_data)

            return HttpResponseRedirect(
                reverse('randevu:day-archive', kwargs={
                    'year': randevu.date.year,
                    'month': randevu.date.month,
                    'day': randevu.date.day
                })
            )
        else:
            return render(request, 'randevu/randevu_form.html', context={'form': form})


class RandevuListView(generic.ListView):
    model = Randevu

    def _get_randevu_list(self, date):
        data = {}

        for randevu in Randevu.objects.filter(date=date, state=Randevu.STATE_OPEN):
            data[randevu.time.strftime("%H:%M")] = {
                'name': randevu.hasta,
                'person_number': str(randevu.person_number)
            }

        return data

    def get(self, request, *args, **kwargs):
        date = request.GET.get('date')

        data = self._get_randevu_list(date)

        return JsonResponse(data)

    def post(self, request, *args, **kwargs):
        return HttpResponseNotAllowed(['POST'])


class RandevuDetailView(generic.DetailView):
    model = Randevu

    def post(self, request, *args, **kwargs):
        return HttpResponseNotAllowed(['POST'])


class RandevuUpdateView(generic.UpdateView):
    model = Randevu
    form_class = RandevuCreateForm


class RandevuCancelView(generic.UpdateView):
    model = Randevu
    form_class = RandevuCreateForm

    def get(self, request, *args, **kwargs):
        return HttpResponseNotAllowed(['GET'])

    def post(self, request, *args, **kwargs):
        randevu_id = request.POST.get('randevu_id')
        try:
            randevu = Randevu.objects.get(pk=randevu_id)
        except Randevu.DoesNotExist:
            return HttpResponse(status=404)

        randevu.state = Randevu.STATE_CANCELLED
        randevu.save()

        return HttpResponseRedirect(
            reverse('randevu:day-archive', kwargs={
                'year': randevu.date.year,
                'month': randevu.date.month,
                'day': randevu.date.day
            })
        )


class RandevuDayArchiveView(generic.DayArchiveView):
    queryset = Randevu.objects.filter(state=Randevu.STATE_OPEN)
    date_field = 'date'
    month_format = '%m'
    allow_future = True


class RandevuTodayArchiveView(generic.TodayArchiveView):
    queryset = Randevu.objects.filter(state=Randevu.STATE_OPEN)
    date_field = 'date'
    allow_future = True


class RandevuWeekArchiveView(generic.WeekArchiveView):
    queryset = Randevu.objects.filter(state=Randevu.STATE_OPEN)
    date_field = 'date'
    week_format = '%W'
    allow_future = True

    def _get_first_day(self, year, week):
        return datetime.strptime('{}-W{}-1'.format(year, week), '%Y-W%W-%w').date()

    def _get_randevu_list(self, date):
        queryset = self.queryset.filter(date=date)
        return queryset if queryset.exists() else None

    def get_context_data(self, **kwargs):
        context = super(RandevuWeekArchiveView, self).get_context_data(**kwargs)

        first_day = self._get_first_day(self.kwargs.get('year'), self.kwargs.get('week'))
        dates = [first_day + timedelta(days=i) for i in range(6)]
        randevu_list_by_date = {date: self._get_randevu_list(date) for date in dates}
        context.update({'randevu_list_by_date': sorted(randevu_list_by_date.items(), key=lambda t: t[0])})

        return context
