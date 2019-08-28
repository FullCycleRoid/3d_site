from django import forms


class OrderForm(forms.ModelForm):
    class Meta:
        model = Contacts