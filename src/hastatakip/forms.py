# -*- coding: utf-8 -*-

from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(
        max_length = 32,
        required = True,
        widget = forms.widgets.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        max_length = 64,
        required = True,
        widget = forms.widgets.PasswordInput(attrs={'class': 'form-control'})
    )
