from django.shortcuts import render

# Create your views here.

def index_view(request):
    return render(request, 'website/index.html')


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
