from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def news(request):
    return render(request, 'news.html')


def feedback(request):
    return render(request, 'patients.html')


def service(request):
    return render(request, 'services.html')
