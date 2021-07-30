from django.views.generic import TemplateView, FormView


class MainTemplateView(TemplateView):
    template_name = "pages/main.html"
    title = 'Главная'

    menu = {'#technologies': 'Технологии', '#materials': 'Материалы', '#price': 'Цены',
            '#equlation': 'Расчет прочности', '#order': 'Заказ и доставка'}


class SinteringTemplateView(TemplateView):
    template_name = "pages/sintering.html"
    title = 'Спекание'

class MetalTemplateView(TemplateView):
    template_name = "pages/metal.html"
    title = 'Металл'


class PrintingTemplateView(TemplateView):
    template_name = "pages/metal.html"
    title = 'Печать'


class FarmTemplateView(TemplateView):
    template_name = "pages/farm.html"
    title = '3D Ферма'


class ContactsTemplateView(TemplateView):
    template_name = "pages/contacts.html"
    title = 'Контакты'


class MaterialsTemplateView(TemplateView):
    template_name = "pages/materials.html"
    title = 'Материалы'


