from django.shortcuts import render, redirect
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
            messages.add_message(request, messages.SUCCESS, "پیام شما با موفقیت ارسال شد.")
            return redirect('/contact')
        else:
            messages.add_message(request, messages.ERROR, "متاسفانه پیام شما ارسال نشد.")
            return redirect('/contact')
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
            print("hi")
            messages.add_message(request, messages.SUCCESS, "ایمیل شما با موفقیت ثبت شد.")
            return HttpResponseRedirect('/')

        else:
            messages.add_message(request, messages.ERROR, "خطا در ثبت ایمیل!")
            return HttpResponseRedirect('/')
