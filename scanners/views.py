from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView
from.models import Scanner

# Create your views here.

class ScannerListView(LoginRequiredMixin,ListView):

    template_name = 'scanners_table.html'

    model = Scanner

    context_object_name = 'scannerslist'

    login_url = 'login'
