from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from .models import StockIn
from django.views.generic import ListView

# Create your views here.

class StockInListView(LoginRequiredMixin,ListView):
    template_name = 'stock_in.html'
    model = StockIn
    context_object_name = 'stockin'
    login_url = 'login'
    
