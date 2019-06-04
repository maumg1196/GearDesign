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

    aligment_choices = (
        ('Open gearing', 'Open gearing'),
        ('Commercial enclosed gear units', 'Commercial enclosed gear units'),
        ('Precision enclosed gear units', 'Precision enclosed gear units'),
        ('Extra-precision enclosed gear units', 'Extra-precision enclosed gear units'),
    )

    Ynp = forms.ChoiceField(
        required=True,
        choices=Ynp_choices,
    )
    Znp = forms.ChoiceField(
        required=True,
        choices=Znp_choices,
    )
    Yng = forms.ChoiceField(
        required=True,
        choices=Ynp_choices,
    )
    Zng = forms.ChoiceField(
        required=True,
        choices=Znp_choices,
    )
    aligment_type = forms.ChoiceField(
        required=True,
        choices=aligment_choices,
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


class GearForm3(forms.ModelForm):
    
    class Meta:
        model = Gear
        fields = [
            'materialp',
            'materialg'
        ]
