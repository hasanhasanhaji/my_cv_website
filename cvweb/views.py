from django.shortcuts import render
from cvweb.forms import NewsletterForm, ContactForm
from django.http import HttpResponseRedirect
# Create your views here.


def index_view(request):
    context = {'name': 'حسن حاجی محمدی',
               'prompt': 'سلام، بنده',
               'dis': 'برنامه نویس، کارآفرین و مدرس دانشگاه هستم.',
               'education': 'دکترای کامپیوتر گرایش هوش مصنوعی'
               }

    return render(request, 'website/index.html', context)


def about_view(request):

    return render(request, 'website/about-us.html')


def contact_view(request):
    return render(request, 'website/contact.html')


def element_view(request):
    return render(request, 'website/elements.html')


def portfolio_view(request):
    return render(request, 'website/portfolio.html')


def service_view(request):
    return render(request, 'website/services.html')


def newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/')
