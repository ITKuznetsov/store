from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'title': 'Store',
    }
    return render(request, 'products/index.html', context=context)


def products(request):
    return render(request, 'products/products.html')
