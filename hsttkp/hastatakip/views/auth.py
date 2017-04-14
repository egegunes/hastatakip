# -*- coding: utf-8 -*-

from django.views.generic.base          import View
from django.template.response           import TemplateResponse
from django.contrib.auth                import authenticate, login, logout
from django.http                        import HttpResponseRedirect
from django.urls                        import reverse

from hastatakip.forms                   import LoginForm

class LoginView(View):
    form_class = LoginForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return TemplateResponse(request, 'login.html', context={'form': form})

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            form = self.form_class()
            return TemplateResponse(request, 'login.html', context={'form': form, 'login_failed': True})

class LogoutView(View):

    def get(self, request, *args, **kwargs):
        logout(request)
        return TemplateResponse(request, 'logged_out.html', context={})
