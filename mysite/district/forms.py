from django import forms

from . import models
from .models import District, Taluka, Village


class DistrictForm(forms.ModelForm):
    class Meta:
        model = District
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class TalukaForm(forms.ModelForm):
    class Meta:
        model = Taluka
        fields = '__all__'
        widgets = {
            'district': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class VillageForm(forms.ModelForm):
    class Meta:
        model = Village
        fields = '__all__'
        widgets = {
            'district': forms.Select(attrs={'class': 'form-control'}),
            'taluka': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['taluka'].queryset = models.Taluka.objects.none()

        if 'taluka' in self.data:
            try:
                district_id = int(self.data.get('district'))
                self.fields['taluka'].queryset = models.Taluka.objects.filter(district_id=district_id).order_by('name')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['taluka'].queryset = self.instance.district.taluka_set.order_by('name')

        # self.fields['village'].queryset = models.Village.objects.none()
        #
        # if 'village' in self.data:
        #     try:
        #         taluka_id = int(self.data.get('taluka'))
        #         self.fields['village'].queryset = models.Village.objects.filter(taluka_id=taluka_id).order_by('name')
        #     except (ValueError, TypeError):
        #         pass
        # elif self.instance.pk:
        #     self.fields['union'].queryset = self.instance.taluka.village_set.order_by('name')
