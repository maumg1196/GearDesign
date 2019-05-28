from django import forms


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
