from django.conf.urls import url
from .views import *

app_name = "main_site"
urlpatterns = [
    url(r'metal/', MetalTemplateView.as_view(), name="metal"),
    url(r'sintering/', SinteringTemplateView.as_view(), name="sintering"),
    url(r'farm/', FarmTemplateView.as_view(), name="farm"),
    url(r'contacts/', ContactsTemplateView.as_view(), name="contacts"),
    url(r'materials/', MaterialsTemplateView.as_view(), name="materials"),
    url(r'^$', MainTemplateView.as_view(), name="main"),
]