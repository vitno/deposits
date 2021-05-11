from django import forms
from deposits_app.models import DepositModel


class DepositForm(forms.ModelForm):
    class Meta:
        model = DepositModel
        fields = [
            'deposit',
            'term',
            'rate',
            'interest',
        ]