from django import forms
from .models import Soldier

class DateInput(forms.DateInput):
    input_type = 'date'

class SoldierCreateForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}), label='비밀번호 확인')
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
            'army_choice' : forms.Select(
                attrs={
                    'class': 'form-select'
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
        cleaned_data = super(SoldierCreateForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "비밀번호가 불일치합니다."
            )

class SoldierUpdateForm(forms.ModelForm):
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
            'army_choice' : forms.Select(
                attrs={
                    'class': 'form-select'
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
        cleaned_data = super(SoldierUpdateForm, self).clean()
        password = cleaned_data.get("password")
        # get password from model instance
        confirm_password = self.instance.password

        if password != confirm_password:
            raise forms.ValidationError(
                "비밀번호가 불일치합니다."
            )

class SoldierDeleteForm(forms.ModelForm):
    class Meta:
        model = Soldier
        fields = [
                    'password',
                ]
        widgets = {
            'password' : forms.PasswordInput(
                attrs={
                    'class': 'form-control'
                }
            ),
        }

    def clean(self):
        cleaned_data = super(SoldierDeleteForm, self).clean()
        password = cleaned_data.get("password")
        # get password from model instance
        confirm_password = self.instance.password


        if password != confirm_password:
            raise forms.ValidationError(
                "비밀번호가 불일치합니다."
            )