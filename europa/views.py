from django.shortcuts import render
from django.http import request

# Create your views here.

def europa(request):
    return render(request, 'index_europa.html')


def alemanha(request):
    return render(request, 'alemanha.html')


def italia(request):
    return render(request, 'italia.html')


def franca(request):
    return render(request, 'franca.html')