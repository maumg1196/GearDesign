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


class GearForm2(forms.ModelForm):

    Ynp_choices = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
    )

    Znp_choices = (
        (1, 1),
        (2, 2),
        (3, 3),
    )

    Ynp = forms.ChoiceField(
        required=True,
        choices=Ynp_choices,
    )
    Znp = forms.ChoiceField(
        required=True,
        choices=Znp_choices,
    )

    class Meta:
        model = Gear
        fields = [
            'Jp',
            'Jg',
            'I',
            'kr',
            'SF',
        ]
        widgets = {
            'Jp': forms.NumberInput(attrs={'step': "0.01"}),
            'Jg': forms.NumberInput(attrs={'step': "0.01"}),
            'I': forms.NumberInput(attrs={'step': "0.01"}),
            'kr': forms.NumberInput(attrs={'step': "0.01"}),
            'SF': forms.NumberInput(attrs={'step': "0.01"}),
        }


class FirstForm(forms.Form):

    Ynp_choices = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
    )

    Znp_choices = (
        (1, 1),
        (2, 2),
        (3, 3),
    )

    Jp = forms.FloatField(
        required=True,
        min_value=0.01,
        widget=forms.NumberInput(attrs={'step': "0.01"})
    )
    Jg = forms.FloatField(
        required=True,
        min_value=0.01,
        widget=forms.NumberInput(attrs={'step': "0.01"})
    )
    I = forms.FloatField(
        required=True,
        min_value=0.01,
        widget=forms.NumberInput(attrs={'step': "0.01"})
    )
    kr = forms.FloatField(
        required=True,
        min_value=0.01,
        widget=forms.NumberInput(attrs={'step': "0.01"})
    )
    SF = forms.FloatField(
        required=True,
        min_value=1.00,
        max_value=1.50,
        widget=forms.NumberInput(attrs={'step': "0.01"})
    )
    Ynp = forms.ChoiceField(
        required=True,
        choices=Ynp_choices,
    )
    Znp = forms.ChoiceField(
        required=True,
        choices=Znp_choices,
    )
