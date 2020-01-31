from django.shortcuts import render
from .models import ServiceProduct, ServiceProductCategory


def price_list(request):
    service_products = ServiceProduct.objects.all()

    return render(request, 'price_list_all.html', {
        'service_products': service_products
    })


def price_list_by_category(request):
    service_products = ServiceProduct.objects.all()
    service_categories = ServiceProductCategory.objects.all()

    return render(request, 'price_categories.html', {
        'products': service_products,
        'categories': service_categories
    })
