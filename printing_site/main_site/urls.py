from django.conf.urls import url
from main_site import views

app_name = "main_site"
urlpatterns = [
    url(r'home/', views.HomeTemplateView.as_view(), name="home"),
    url(r'model/', views.ModelTemplateView.as_view(), name="model"),
    url(r'scan/', views.ScanTemplateView.as_view(), name="scan"),
    url(r'mould/', views.MouldTemplateView.as_view(), name="mould"),
    url(r'contacts/', views.ContactsTemplateView.as_view(), name="contacts"),
    url(r'rezka/', views.RezkaTemplateView.as_view(), name="rezka"),
    url(r'^$', views.IndexTemplateView.as_view(), name="index"),
]