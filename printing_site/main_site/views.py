from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView
from main_site.forms import OrderForm
from sendemail.forms import ContactForm

# Create your views here.


class IndexTemplateView(FormView):
    template_name = "main_site/index.html"
    title = '3D печать'

    menu = {'#technology':'Технологии','#materials':'Материалы','#price':'Цены',
            '#equlation':'Расчет прочности','#order':'Заказ и доставка'}

    form_class = ContactForm
    success_url = 'success'

class HomeTemplateView(TemplateView):
    template_name = "main_site/home.html"
    title = 'Главная'

class ScanTemplateView(TemplateView):
    template_name = "main_site/scan.html"
    title = '3D сканирование'

class ModelTemplateView(TemplateView):
    template_name = "main_site/model.html"
    title = 'Моделирование'

    menu = {'#3dmax':'Поверхностное','#solid':'Твердотельное'}


class MouldTemplateView(TemplateView):
    template_name = "main_site/mould.html"
    title = 'Литье'

class ContactsTemplateView(TemplateView):
    template_name = "main_site/contacts.html"
    title = 'Контакты'


class RezkaTemplateView(TemplateView):
    template_name = "main_site/rezka.html"
    title = 'Лазерная резка'


