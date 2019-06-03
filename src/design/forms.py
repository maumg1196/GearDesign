from django import forms 
from .models import Gear


class GearForm(forms.ModelForm):

    class Meta:
        model = Gear
        fields = [
            'fs',
            'HP',
            'Np',
            'Pd',
            'Wg',
            'Wp',
        ]
        widgets = {
            'fs': forms.NumberInput(attrs={'step': "0.01"}),
            'HP': forms.NumberInput(attrs={'step': "0.01"}),
            'Pd': forms.NumberInput(attrs={'step': "0.01"}),
            'Wg': forms.NumberInput(attrs={'step': "0.01"}),
            'Wp': forms.NumberInput(attrs={'step': "0.01"}),
        }


class GearForm(forms.ModelForm):

    class Meta:
        model = Gear
        fields = [
            'fs',
            'HP',
            'Np',
            'Pd',
            'Wg',
            'Wp',
            'q',
            'hrs',
            'Ep',
            'Eg',
            'Vp',
            'Vg',
        ]
        widgets = {
            'fs': forms.NumberInput(attrs={'step': "0.01"}),
            'HP': forms.NumberInput(attrs={'step': "0.01"}),
            'Pd': forms.NumberInput(attrs={'step': "0.01"}),
            'Wg': forms.NumberInput(attrs={'step': "0.01"}),
            'Wp': forms.NumberInput(attrs={'step': "0.01"}),
            'hrs': forms.NumberInput(attrs={'step': "0.01"}),
            'q': forms.NumberInput(attrs={'step': "0.01"}),
            'Ep': forms.NumberInput(attrs={'step': "0.01"}),
            'Eg': forms.NumberInput(attrs={'step': "0.01"}),
            'Vp': forms.NumberInput(attrs={'step': "0.01"}),
            'Vg': forms.NumberInput(attrs={'step': "0.01"}),
        }


class FirstForm(forms.Form):

    fs = forms.FloatField(
        required=True,
        min_value=0.01,
        widget=forms.NumberInput(attrs={'step': "0.01"})
    )
    HP = forms.FloatField(
        required=True,
        min_value=0.01,
        widget=forms.NumberInput(attrs={'step': "0.01"})
    )
    Np = forms.FloatField(
        required=True,
        min_value=0.01,
        widget=forms.NumberInput(attrs={'step': "0.01"})
    )
    Pd = forms.FloatField(
        required=True,
        min_value=0.01,
        widget=forms.NumberInput(attrs={'step': "0.01"})
    )
    Wg = forms.FloatField(
        required=True,
        min_value=0.01,
        widget=forms.NumberInput(attrs={'step': "0.01"})
    )
    Wp = forms.FloatField(
        required=True,
        min_value=0.01,
        widget=forms.NumberInput(attrs={'step': "0.01"})
    )
