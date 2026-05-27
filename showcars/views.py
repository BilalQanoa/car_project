from django.shortcuts import render
from django.views import generic

# Create your views here.
class ShowCars (generic.TemplateView):
    template_name = 'show_cars.html'

    