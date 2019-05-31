"""Design's Views."""
import math
from .forms import (
    GearForm,
    FirstForm,
)
from .models import Gear
from django.urls import reverse
from django.views.generic import (
    TemplateView,
    CreateView,
    FormView,
)
from django.contrib.auth.mixins import LoginRequiredMixin


class GearCreate(LoginRequiredMixin, CreateView):

    model = Gear
    form_class = GearForm
    template_name = "first.html"

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save(commit=False)
        self.object.user = self.request.user

        fs = self.object.fs
        HP = self.object.HP
        Np = self.object.Np
        Pd = self.object.Pd
        Wg = self.object.Wg
        Wp = self.object.Wp

        PotD = HP * fs
        Ng = round((Wp / Wg) * Np)
        Dp = Np / Pd
        Vt = round((math.pi * Dp * Wp) / 12, 2)
        C = round((Np + Ng) / (2 * Pd), 2)
        Ft = round((33000 * PotD) / Vt, 2)
        F = 12 / Pd
        if Vt < 800:
            A = 10
        elif 800 <= Vt < 2000:
            A = 8
        elif 2000 <= Vt < 4000:
            A = 6
        else:
            A = 4
        B = 0.25 * ((A - 5)**0.667)
        Cprime = 50 + (56 * (1 - B))
        kv = round((Cprime / (Cprime + math.sqrt(Vt)))**(-B), 4)
        if F < 1:
            Cpf = (F / (10 * Dp)) - 0.025
        else:
            Cpf = (F / (10 * Dp)) - 0.0375 + (0.0125 * F)
        Cpf = round(Cpf, 4)

        self.object.PotD = PotD
        self.object.Ng = Ng
        self.object.Dp = Dp
        self.object.Vt = Vt
        self.object.C = C
        self.object.Ft = Ft
        self.object.F = F
        self.object.Av = A
        self.object.kv = kv
        self.object.Cpf = Cpf

        self.object.save()
        return super(GearCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse('design:first')


class FirstView(LoginRequiredMixin, FormView):
    """This view recibe form fields and send an email."""

    template_name = 'first.html'
    form_class = FirstForm
    fs = ""
    HP = ""
    Np = ""
    Pd = ""
    Wg = ""
    Wp = ""

    def form_valid(self, form):
        self.fs = form.cleaned_data['fs']
        self.HP = form.cleaned_data['HP']
        self.Np = form.cleaned_data['Np']
        self.Pd = form.cleaned_data['Pd']
        self.Wg = form.cleaned_data['Wg']
        self.Wp = form.cleaned_data['Wp']
        return super(FirstView, self).form_valid(form)

    def get_success_url(self):
        url = '/second/?fs={}&HP={}&Np={}&Pd={}&Wg={}&Wp={}'.format(
            self.fs,
            self.HP,
            self.Np,
            self.Pd,
            self.Wg,
            self.Wp,
        )
        return url


class SecondView(LoginRequiredMixin, TemplateView):

    template_name = "second.html"

    def get_context_data(self, **kwargs):
        context = super(SecondView, self).get_context_data(**kwargs)
        context['fs'] = float(self.request.GET.get('fs'))
        context['HP'] = float(self.request.GET.get('HP'))
        context['Np'] = float(self.request.GET.get('Np'))
        context['Pd'] = float(self.request.GET.get('Pd'))
        context['Wg'] = float(self.request.GET.get('Wg'))
        context['Wp'] = float(self.request.GET.get('Wp'))
        fs = context['fs']
        HP = context['HP']
        Np = context['Np']
        Pd = context['Pd']
        Wg = context['Wg']
        Wp = context['Wp']
        PD = HP * fs
        Ng = round((Wp / Wg) * Np)
        Dp = Np / Pd
        Vt = round((math.pi * Dp * Wp) / 12, 2)
        C = round((Np + Ng) / (2 * Pd), 2)
        Ft = round((33000 * PD) / Vt, 2)
        F = 12 / Pd
        if Vt < 800:
            A = 10
        elif 800 <= Vt < 2000:
            A = 8
        elif 2000 <= Vt < 4000:
            A = 6
        else:
            A = 4
        B = 0.25 * ((A - 5)**0.667)
        Cprime = 50 + (56 * (1 - B))
        kv = round((Cprime / (Cprime + math.sqrt(Vt)))**(-B), 4)
        if F < 1:
            Cpf = (F / (10 * Dp)) - 0.025
        else:
            Cpf = (F / (10 * Dp)) - 0.0375 + (0.0125 * F)
        Cpf = round(Cpf, 4)
        context['PD'] = PD
        context['Ng'] = Ng
        context['Dp'] = Dp
        context['Vt'] = Vt
        context['C'] = C
        context['Ft'] = Ft
        context['F'] = F
        context['Av'] = 'A' + str(A)
        context['kv'] = kv
        context['Cpf'] = Cpf
        return context
