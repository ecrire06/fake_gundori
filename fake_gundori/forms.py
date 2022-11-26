from django import forms
from .models import Soldier

class DateInput(forms.DateInput):
    input_type = 'date'

class SoldierForm(forms.ModelForm):
    class Meta:
        model = Soldier
        fields = [
                    'name',
                    'enter_date',
                    'army_choice',
                    'bio',
                    'password',
                ]
        widgets = {
            'enter_date' : DateInput(),
            'password' : forms.PasswordInput(),
        }