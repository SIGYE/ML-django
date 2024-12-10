from django import forms
from .models import HousingApplication

class HousingApplicationForm(forms.ModelForm):
    class Meta:
        model = HousingApplication
        fields = ['tenant', 'application_date', 'status']
