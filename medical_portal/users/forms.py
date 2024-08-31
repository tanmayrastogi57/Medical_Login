from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import PatientProfile, DoctorProfile


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class PatientProfileForm(forms.ModelForm):
    class Meta:
        model = PatientProfile
        fields = ['address_line1', 'city', 'state', 'pincode', 'profile_picture']


class DoctorProfileForm(forms.ModelForm):
    class Meta:
        model = DoctorProfile
        fields = ['specialization', 'profile_picture','address_line1', 'city', 'state', 'pincode']
