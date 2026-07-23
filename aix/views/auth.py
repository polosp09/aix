"""
Contributions to this module:
Miguel Sanda <msanda@arrobalytics.com>
Mando <mandonpolo@gmail.com>
"""

from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse, reverse_lazy
from django.utils.translation import gettext_lazy as _

from aix.forms.auth import LogInForm


class DjangoLedgerLoginView(LoginView):
    form_class = LogInForm
    #template_name = 'aix/auth/login.html'
    template_name = 'aix/pages/authentication/auth-login.html'
    extra_context = {
        'page_title': _('Login')
    }

    def get_success_url(self):
        return reverse('aix:home')


class DjangoLedgerLogoutView(LogoutView):
    next_page = reverse_lazy('aix:login')
