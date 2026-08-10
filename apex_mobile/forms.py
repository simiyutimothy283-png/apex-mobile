from django import forms
from .models import RegisteredClient

class ClientRegistrationForm(forms.ModelForm):
    class Meta:
        model = RegisteredClient
        fields = ['name', 'email', 'phone_number']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 bg-slate-800 text-white border border-slate-700 rounded-lg focus:outline-none focus:border-blue-500',
                'placeholder': 'Your Full Name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full px-4 py-2 bg-slate-800 text-white border border-slate-700 rounded-lg focus:outline-none focus:border-blue-500',
                'placeholder': 'name@example.com'
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 bg-slate-800 text-white border border-slate-700 rounded-lg focus:outline-none focus:border-blue-500',
                'placeholder': 'e.g. +254 711 011011'
            }),
        }