from django.urls import path, include
from django.views.generic import TemplateView
from .views import ContactUsView

urlpatterns = [
    path('about-us/', TemplateView.as_view(template_name='main/about_us.html'), name='about_us'),
    path('contact-us/', ContactUsView.as_view(), name='contact_us'),
    path('', TemplateView.as_view(template_name='main/home.html'), name='home'),
]
