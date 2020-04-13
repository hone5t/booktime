import logging
logger = logging.getLogger(__name__)

from django import forms
from django.core.mail import send_mail

class ContactForm(forms.Form):
    name = forms.CharField(label = 'Your Name', max_length=100)
    message = forms.CharField(max_length=600, widget = forms.Textarea)

    def send_mail(self):
        logger.info("Sending email to customer service")
        name = self.cleaned_data['name']
        msg = self.cleaned_data['message']
        message = f"From {name} \n {msg}"
        send_mail(
            "Site Message",
            message,
            ["admin@admin.com"],
            ["admin@admin.com"],
            fail_silently = False
        )