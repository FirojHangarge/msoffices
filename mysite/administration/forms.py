from django import forms
from . import models



class DepartmentForm(forms.ModelForm):
    class Meta:
        model = models.Department
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class LoanTypeForm(forms.ModelForm):
    class Meta:
        model = models.LoanType
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class ReportTypeForm(forms.ModelForm):
    class Meta:
        model = models.ReportType
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }



class PropertyTypeForm(forms.ModelForm):
    class Meta:
        model = models.PropertyType
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class ConstructionTypeForm(forms.ModelForm):
    class Meta:
        model = models.ConstructionType
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }