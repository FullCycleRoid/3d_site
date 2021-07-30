from django import forms
from .models import Contacts


class OrderForm(forms.ModelForm):
    # file = forms.FileField()
    # message = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Contacts
        fields = ['name', 'email', 'phone_number']
