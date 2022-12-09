from django import forms
from .models import Soldier

class DateInput(forms.DateInput):
    input_type = 'date'

class SoldierForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput())
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
            'name' : forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'enter_date' : DateInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'bio' : forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'password' : forms.PasswordInput(
                attrs={
                    'class': 'form-control'
                }
            ),
        }

    def clean(self):
        cleaned_data = super(SoldierForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "비밀번호와 불일치합니다."
            )