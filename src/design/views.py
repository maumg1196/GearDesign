import math
from .forms import *
from django.views.generic import (
    TemplateView,
    FormView,
)
from django.urls import reverse_lazy


class FirstView(FormView):
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


class SecondView(TemplateView):

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
        PD = HP*fs
        Ng = (Wp/Wg)*Np
        Dp = Np/Pd
        Vt = (math.pi*Dp*Wp)/12
        C = (Np + Ng)/(2*Pd)
        Ft = (33000*PD)/Vt
        F = 12/Pd
        context['PD'] = PD
        context['Ng'] = Ng
        context['Dp'] = Dp
        context['Vt'] = Vt
        context['C'] = C
        context['Ft'] = Ft
        context['F'] = F
        return context
