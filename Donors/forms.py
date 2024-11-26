from django import forms
from .models import Donor

class DonorRegistrationForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = ['name', 'desig', 'mobile_number', 'bcs_batch', 'blood_group', 'last_blood_donation', 'is_available']

class UpdateDonationForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = ['last_blood_donation', 'is_available']
