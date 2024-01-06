
from cvweb.models import Contact, Newsletter
from django.forms import ModelForm
from captcha.fields import CaptchaField


class ContactForm(ModelForm):
    captcha = CaptchaField()  # it's for captcha
    class Meta:
        model = Contact
        fields = '__all__'  # چه فیلدهایی داشته باشه فرم من



class NewsletterForm(ModelForm):
    class Meta:
        model = Newsletter
        fields = '__all__'