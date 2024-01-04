
from cvweb.models import Contact, Newsletter
from django.forms import ModelForm


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'  # چه فیلدهایی داشته باشه فرم من


class NewsletterForm(ModelForm):
    class Meta:
        model = Newsletter
        fields = '__all__'