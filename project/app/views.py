from django.shortcuts import render
from django.views.generic import ListView
from app.models import AccordionItem

# Create your views here.
class Accord(ListView):
    model = AccordionItem
    context_object_name = 'items'
    template_name = 'index.html'