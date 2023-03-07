from django.shortcuts import render
from django.http import request

# Create your views here.

def america(request):
    return render(request, 'index_america.html')


def brasil(request):
    return render(request, 'brasil.html')


def argentina(request):
    return render(request, 'argentina.html')