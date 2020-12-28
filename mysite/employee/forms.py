from django import forms
from . import models
from bootstrap_datepicker_plus import DatePickerInput




class PersonalInfoForm(forms.ModelForm):
    class Meta:
        model = models.PersonalInfo
        fields = '__all__'
        exclude = {'date_of_resignation', 'is_delete', }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'department': forms.Select(attrs={'class': 'form-control'}),
            'date_of_joining': DatePickerInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'phone_no': forms.NumberInput(attrs={'class': 'form-control'}),
            'home_phone': forms.NumberInput(attrs={'class ': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'resume': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'id_proof': forms.ClearableFileInput(attrs={'class': 'form-control'}),



        }
