from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from order.models import OrderItem
from django.views.generic import ListView

# Create your views here.

class OrderItemList(ListView):

    model = OrderItem
    template_name = 'ordered_item.html'
    context_object_name = 'ordered_item'
