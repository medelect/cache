from django import forms
from wtforms_alchemy import ModelForm
from .models import Income


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)


class IncomeForm(ModelForm):
    class Meta:
        model = Income
        include_primary_keys = True
