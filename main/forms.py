from django import forms
from .models import Contact

class ContactForm (forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

        labels = {
            'name' : 'Full Name',
            'email' : 'Email Address',
            'message' : 'Message'
        }

        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'John Doe'}),
            'email' : forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'name@example.com'}),
            'message' : forms.Textarea(attrs={'class': 'form-control', 'rows': 6, 'placeholder': 'How can we help you today?'}),
        }
