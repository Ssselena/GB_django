from django.shortcuts import render
from .models import ProductCategory, Product

# Create your views here.


def main(request):
    title = 'Surfhouse'
    products = Product.objects.all()[:4]
    content = {'title': title, 'products': products}

    return render(request, 'mainapp/main.html', content)


def products(request):
    return render(request, 'mainapp/products.html', context={'username': 'julia'})


def contacts(request):
    return render(request, 'mainapp/contacts.html', context={'username': 'julia'})

