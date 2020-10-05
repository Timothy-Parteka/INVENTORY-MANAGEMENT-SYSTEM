from django.shortcuts import render
from .models import Faulty
from django.views.generic import ListView

# Create your views here.

class FaultyListView(ListView):
    template_name = 'faulty_items.html'
    model = Faulty
    context_object_name = 'faultylist'
    
