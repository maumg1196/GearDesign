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
    UpdateView,
    DetailView,
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

        a = round(1 / Pd, 4)
        b = round(1.25 / Pd, 4)
        c = round(0.25 / Pd, 4)

        Dep = round((Np + 2) / Pd, 4)
        Deg = round((Ng + 2) / Pd, 4)

        Dg = (2 * C) / Dp
        Drp = Dp - (2 * b)
        Drg = Dg - (2 * b)

        ht = a + b
        hk = 2 * a
        t = math.pi / (2 * Pd)

        self.object.PotD = PotD
        self.object.Ng = Ng
        self.object.Dp = Dp
        self.object.Dg = Dg
        self.object.Vt = Vt
        self.object.C = C
        self.object.Ft = Ft
        self.object.F = F
        self.object.Av = A
        self.object.kv = kv
        self.object.Cpf = Cpf
        self.object.addendum = a
        self.object.dedendum = b
        self.object.clair = c
        self.object.Dep = Dep
        self.object.Deg = Deg
        self.object.Drp = Drp
        self.object.Drg = Drg
        self.object.depth_total = ht
        self.object.work_depth = hk
        self.object.t = t

        self.object.save()
        return super(GearCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse('design:first')


class SecondView(LoginRequiredMixin, UpdateView):

    model = Gear
    template_name = "second.html"

    def get_context_data(self, **kwargs):
        context = super(SecondView, self).get_context_data(**kwargs)
        return context


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
