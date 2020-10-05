from django.shortcuts import render

from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm

# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
