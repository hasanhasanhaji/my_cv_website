from django.shortcuts import render
from cvweb.forms import NewsletterForm, ContactForm
from django.http import HttpResponseRedirect
from django.contrib import messages
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
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Your ticket submitted very well")
        else:
            messages.add_message(request, messages.ERROR, "Your ticket didnt submitted successfully")
    form = ContactForm()
    return render(request, 'website/contact.html', {'form': form})


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
            messages.add_message(request, messages.SUCCESS, "Your ticket submitted very well")
            return HttpResponseRedirect('/')

        else:
            messages.add_message(request, messages.ERROR, "Your ticket didnt submitted successfully")
            return HttpResponseRedirect('/')
