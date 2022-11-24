from django import forms
from django.forms import ModelForm
from .models import Soldier

class DateInput(forms.DateInput):
    input_type = 'date'

class SoldierForm(ModelForm):
    class Meta:
        model = Soldier
        fields = ['name', 'enter_date', 'army_choice', 'bio']
        widgets = {
            'enter_date' : DateInput(),
        }