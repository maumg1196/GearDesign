"""Design's Views."""
import math
from .forms import (
    GearForm,
    GearForm2,
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
        hrs = self.object.hrs
        q = self.object.q
        Ep = self.object.Ep
        Eg = self.object.Eg
        Vp = self.object.Vp
        Vg = self.object.Vg

        P = round(math.pi / Pd, 4)

        if Pd >= 5:
            self.object.ks = 1.0
        elif 4 <= Pd < 5:
            self.object.ks = 1.05
        elif 3 <= Pd < 4:
            self.object.ks = 1.15
        elif 2 <= Pd < 3:
            self.object.ks = 1.25
        elif 1.25 <= Pd < 2:
            self.object.ks = 1.40

        if self.object.Np == 18.0:
            self.object.angle = 20.0
        elif self.object.Np == 12.0:
            self.object.angle = 25.0
        elif self.object.Np == 32.0:
            self.object.angle = 14.5

        angle = self.object.angle

        PotD = HP * fs
        Ng = round((Wp / Wg) * Np)
        Dp = Np / Pd
        Dg = Ng / Pd
        Vt = round((math.pi * Dp * Wp) / 12, 4)
        C = round((Np + Ng) / (2 * Pd), 4)
        Ft = round((33000 * PotD) / Vt, 4)
        F = 12 / Pd

        ctecpp = (1 - (Vp**2)) / Ep
        ctecpg = (1 - (Vg**2)) / Eg
        denom = math.pi * (ctecpp + ctecpg)
        Cp = math.sqrt(1 / denom)

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

        Drp = round(Dp - (2 * b), 4)
        Drg = round(Dg - (2 * b), 4)

        ht = a + b
        hk = 2 * a
        t = round(math.pi / (2 * Pd), 4)

        L = hrs * 365 * 5
        Ncp = 60 * L * q * Wp
        Ncg = 60 * L * q * Wg

        Dbp = round(Dp * math.cos(math.radians(angle)), 4)
        Dbg = round(Dg * math.cos(math.radians(angle)), 4)

        self.object.PotD = PotD
        self.object.Ng = Ng
        self.object.Dp = Dp
        self.object.Dg = Dg
        self.object.Vt = Vt
        self.object.C = C
        self.object.Ft = Ft
        self.object.F = F
        self.object.P = P
        self.object.Cp = Cp
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
        self.object.Dbp = Dbp
        self.object.Dbg = Dbg
        self.object.L = L
        self.object.Ncp = Ncp
        self.object.Ncg = Ncg

        self.object.save()
        return super(GearCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse('design:continue', kwargs={'gear_id': self.object.id})


class SecondView(LoginRequiredMixin, UpdateView):

    model = Gear
    form_class = GearForm2
    pk_url_kwarg = 'gear_id'
    context_object_name = 'gear'
    template_name = "second.html"

    def form_valid(self, form):
        self.object = form.save(commit=False)

        Ynp_choice = form.cleaned_data['Ynp']
        Znp_choice = form.cleaned_data['Znp']
        aligment_type_choice = form.cleaned_data['aligment_type']

        if aligment_type_choice == 'Open gearing':
            Cma = 0.247 + (0.0167 * self.object.F) - (0.765 * (10**-4) * (self.object.F ** 2))
        elif aligment_type_choice == 'Commercial enclosed gear units':
            Cma = 0.127 + (0.0158 * self.object.F) - (1.093 * (10**-4) * (self.object.F ** 2))
        elif aligment_type_choice == 'Precision enclosed gear units':
            Cma = 0.0657 + (0.0128 * self.object.F) - (0.926 * (10**-4) * (self.object.F ** 2))
        elif aligment_type_choice == 'Extra-precision enclosed gear units':
            Cma = 0.0380 + (0.0102 * self.object.F) - (0.822 * (10**-4) * (self.object.F ** 2))
        self.object.Cma = round(Cma, 4)

        if Ynp_choice == '1':
            Ynp = 9.4518 * (self.object.Ncp**-0.148)
        elif Ynp_choice == '2':
            Ynp = 6.1514 * (self.object.Ncp**-0.1192)
        elif Ynp_choice == '3':
            Ynp = 4.9404 * (self.object.Ncp**-0.1045)
        elif Ynp_choice == '4':
            Ynp = 3.517 * (self.object.Ncp**-0.0817)
        elif Ynp_choice == '5':
            Ynp = 2.3194 * (self.object.Ncp**-0.0538)
        elif Ynp_choice == '6':
            Ynp = 1.3558 * (self.object.Ncp**-0.0178)
        self.object.Ynp = round(Ynp, 4)

        if Znp_choice == '1':
            Znp = 2.466 * (self.object.Ncp**-0.056)
        elif Znp_choice == '2':
            Znp = 1.249 * (self.object.Ncp**-0.0138)
        elif Znp_choice == '3':
            Znp = 1.4488 * (self.object.Ncp**-0.023)
        self.object.Znp = round(Znp, 4)

        return super(SecondView, self).form_valid(form)

    def get_success_url(self):
        return reverse('design:first')


class FirstView(LoginRequiredMixin, FormView):
    """This view recibe form fields and send an email."""

    template_name = 'test.html'
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
