from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def lodge(request):
    return render(request, 'main/lodge.html')


def history(request):
    return render(request, 'main/history.html')


def principles(request):
    return render(request, 'main/principles.html')