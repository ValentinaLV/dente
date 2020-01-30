from django.shortcuts import render


def contact(request):
    return render(request, 'contact.html')


def service(request):
    return render(request, 'services.html')


def price_list(request):
    return render(request, 'pricing.html')
