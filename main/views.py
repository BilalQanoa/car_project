from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .forms import ContactForm
# Create your views here.

class Index (generic.CreateView):
    form_class = ContactForm
    template_name = "landing_page.html"
    success_url = reverse_lazy('index')
