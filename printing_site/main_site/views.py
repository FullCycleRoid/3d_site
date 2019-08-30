from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView
from main_site.forms import OrderForm

# Create your views here.
from main_site.models import Contacts


class IndexTemplateView(TemplateView):
    template_name = "main_site/index.html"
    title = 'index'


class ModelTemplateView(TemplateView):
    template_name = "main_site/model.html"
    title = 'model'


class HomeTemplateView(TemplateView):
    template_name = "main_site/home.html"
    title = 'home'

class ScanTemplateView(TemplateView):
    template_name = "main_site/scan.html"
    title = 'scan'

class MouldTemplateView(TemplateView):
    template_name = "main_site/mould.html"
    title = 'mould'

class ContactsTemplateView(FormView):
    template_name = "main_site/contacts.html"
    title = 'contacts'
    form_class = OrderForm
    success_url = '/'

    def form_valid(self, form):

        Contacts.objects.create(**form.cleaned_data)

        return redirect(self.get_success_url())


class RezkaTemplateView(TemplateView):
    template_name = "main_site/rezka.html"
    title = 'rezka'
