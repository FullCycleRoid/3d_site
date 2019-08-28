from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.



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

class ContactsTemplateView(TemplateView):
    template_name = "main_site/contacts.html"
    title = 'contacts'

class RezkaTemplateView(TemplateView):
    template_name = "main_site/rezka.html"
    title = 'rezka'
