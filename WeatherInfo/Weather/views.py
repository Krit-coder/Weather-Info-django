from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm
import os

# Create your views here.
def index(request):
    cities = City.objects.all()

link = os.getenv('API_LINK')
url = link

if request.method == 'POST':
    form = CityForm(request.POST)
    form.save()

form = CityForm()

weather_data = []

