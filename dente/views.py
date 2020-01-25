from django.shortcuts import render


def contact(request):
    return render(request, 'contact.html')


def news(request):
    return render(request, 'news.html')


def feedback(request):
    return render(request, 'patients.html')


def service(request):
    return render(request, 'services.html')


def price_list(request):
    return render(request, 'pricing.html')
