from django.shortcuts import render
from .models import Product


def index(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'myapp/index.html', context)


def about(request):
    return render(request, 'myapp/about.html')


def site_settings(request):
    return render(request, 'myapp/site_settings.html')


def contact(request):
    return render(request, 'myapp/contact.html')
