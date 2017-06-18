# -*- coding: utf-8 -*-

import datetime

def get_user(request):
    return {
        'user': request.user
    }

def get_week_month_year(request):
    return {
        'cweek': datetime.date.today().isocalendar()[1],
        'cmonth': datetime.date.today().month,
        'cyear': datetime.date.today().year
    }
