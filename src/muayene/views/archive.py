# -*- coding: utf-8 -*-

import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.dates import (
    ArchiveIndexView,
    TodayArchiveView,
    WeekArchiveView,
    MonthArchiveView,
    YearArchiveView,
)
from django.views.generic.edit import FormView
from django.views.generic.base import View
from django.template.response import TemplateResponse
from django.http import HttpResponseNotAllowed

from muayene.forms import DateRangeForm
from muayene.models import Muayene


class MuayeneArchiveView(LoginRequiredMixin, FormView):
    """
    List muayene entries created between specific dates provided from user.
    Ordered by entry id, decreasing.

    URL: /muayene/arsiv
    """

    login_url = "/login/"
    form_class = DateRangeForm
    template_name = "muayene/muayene_archive.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        context = {
            "form": form,
        }
        return TemplateResponse(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            start = form.cleaned_data["start_date"]
            end = form.cleaned_data["end_date"]
            queryset = Muayene.objects.filter(
                tarih__gte=start, tarih__lte=end
            ).order_by("-id")
            context = {"form": form, "start": start, "end": end, "range_list": queryset}
            return TemplateResponse(request, self.template_name, context)


class MuayeneLastCreatedView(LoginRequiredMixin, View):
    """
    List muayene entries created between current date and day before.
    Ordered by entry id, decreasing.

    URL: /muayene/list/son
    """

    login_url = "/login/"
    template_name = "muayene/muayene_list.html"

    def get(self, request, *args, **kwargs):
        today = datetime.date.today()
        yesterday = today - datetime.timedelta(days=1)
        queryset = Muayene.objects.filter(
            tarih__gte=yesterday, tarih__lte=today
        ).order_by("-id")

        return TemplateResponse(request, self.template_name, {"muayene_list": queryset})

    def post(self, request, *args, **kwargs):
        return HttpResponseNotAllowed(["POST"])


class MuayeneWeekArchiveView(LoginRequiredMixin, WeekArchiveView):
    """
    List muayene entries created inside current week.
    Ordered by entry id, decreasing.

    URL: /muayene/arsiv/<year>/hafta/<week>
    <year>: Year with century as a decimal number (e.g 2016, 1995)
    <week>: Week number of the year (Monday as the first day of the week) as a decimal number [00,53]

    context_object_name: object_list
    """

    login_url = "/login/"
    date_field = "tarih"
    week_format = "%W"
    allow_empty = True
    allow_future = True
    queryset = Muayene.objects.all().order_by("-id")

    def post(self, request, *args, **kwargs):
        return HttpResponseNotAllowed(["POST"])


class MuayeneMonthArciveView(LoginRequiredMixin, MonthArchiveView):
    """
    List muayene entries created inside current month.
    Ordered by entry id, decreasing.

    URL: /muayene/arsiv/<year>/<month>
    <year>: Year with century as a decimal number (e.g 2016, 1995)
    <month>: Month as a decimal number [01,12]

    context_object_name: object_list
    """

    login_url = "/login/"
    date_field = "tarih"
    month_format = "%m"
    allow_empty = True
    allow_future = True
    queryset = Muayene.objects.all().order_by("-id")

    def post(self, request, *args, **kwargs):
        return HttpResponseNotAllowed(["POST"])


class MuayeneYearArchiveView(LoginRequiredMixin, YearArchiveView):
    """
    List muayene entries created inside current year.
    Ordered by entry id, decreasing.

    URL: /muayene/arsiv/<year>
    <year>: Year with century as a decimal number (e.g 2016, 1995)

    context_object_name: object_list
    """

    login_url = "/login/"
    date_field = "tarih"
    year_format = "%Y"
    allow_empty = True
    allow_future = True
    make_object_list = True
    queryset = Muayene.objects.all().order_by("-id")

    def post(self, request, *args, **kwargs):
        return HttpResponseNotAllowed(["POST"])
