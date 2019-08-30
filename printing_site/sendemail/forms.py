# sendemail/forms.py
from django import forms
from django.core.validators import RegexValidator


class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True, label='Ваша почта')
    subject = forms.CharField(required=False, label='Тема сообщения')
    phone_regex = RegexValidator(regex=r'^\+?7?\d{9,12}$',
                                 message="Неверный формат номера телефона.")
    phone_number = forms.CharField(validators=[phone_regex], max_length=12, label='Номер телефона', )

    message = forms.CharField(widget=forms.Textarea, required=False, label='Сообщение')
    File = forms.FileField(label='Отправвить модель STL')