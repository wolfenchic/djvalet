from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from services.models import Services


# Create your views here.
def get_home_page(request):
  services = Services.objects.all()
  return render(request, 'home.html', {'services': services})