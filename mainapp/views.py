from django.shortcuts import render

# Create your views here.


def main(request):
    return render(request, 'mainapp/main.html', context={'username': 'julia'})


def products(request):
    return render(request, 'mainapp/products.html', context={'username': 'julia'})


def contacts(request):
    return render(request, 'mainapp/contacts.html', context={'username': 'julia'})

