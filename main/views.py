from django.shortcuts import render
from django.views.generic.edit import FormView
from . import forms

# Create your views here.
class ContactUsView(FormView):
    template_name = "main/contact_us.html"
    form_class = forms.ContactForm
    success_url = "/"
    def form_valid(self, form):
        form.send_mail()
        return super().form_valid(form)