from django import forms
from wtforms_alchemy import ModelForm
from .models import Income, Bill, Inflow, Groups

from wtforms.fields import DateField,  TextField, IntegerField
from wtforms.validators import Email


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)


class BillForm(ModelForm):
    class Meta:
        model = Bill


class IncomeForm(ModelForm):
    class Meta:
        model = Income


class InflowForm(ModelForm):
    class Meta:
        model = Inflow


class GroupsForm(ModelForm):
    class Meta:
        model = Groups


