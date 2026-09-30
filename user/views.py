from django.shortcuts import render


def home(request):
    return render(request, 'index.html')


def boshlash(request):
    return render(request, 'boshlash.html')


def registratsiya(request):
    return render(request, 'registratsiya.html')


def tashkilot(request):
    return render(request, 'tashkilot.html')


def yordam(request):
    return render(request, 'yordam.html')


def kabinet(request):
    return render(request, 'kabinet.html')
