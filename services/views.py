from django.shortcuts import render, get_object_or_404, redirect, reverse, HttpResponse
from django.http import HttpResponse
from .models import Services

# Create your views here.

def get_services_page(request):
    services = Services.objects.all()
    return render(request, 'services.html', {'services': services})

