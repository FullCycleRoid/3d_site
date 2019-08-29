from django import forms
from django.core.mail import send_mail
from main_site.models import Contacts


class OrderForm(forms.ModelForm):
    # file = forms.FileField()
    # message = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Contacts
        fields = ['name', 'email', 'phone_number']
