from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from bankinghall.models import BankingHallDesktop, BankingHallBarcodeScanner
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

# Create your views here.

class BankingHallDesktopListView(LoginRequiredMixin, ListView):

    model= BankingHallDesktop

    template_name= 'banking_hall_desktop_table.html'

    context_object_name= 'banking_hall_desktop_table'

    login_url = 'login'


class BankingHallDesktopDetailView(LoginRequiredMixin, DetailView):

    model= BankingHallDesktop

    template_name= 'banking_hall_desktop_detail.html'

    login_url = 'login'



class BankingHallDesktopCreateView(LoginRequiredMixin, CreateView):

    model = BankingHallDesktop

    template_name = 'banking_hall_desktop_create.html'

    fields = ('cpu_serial_number', 'monitor_serial_number', 'keyboard_serial_number', 'description', 'floor_location')

    success_url = reverse_lazy('bankinghalldesktoptable')

    login_url = 'login'


    def form_valid(self, form):

        form.instance.updated_by = self.request.user

        return super().form_valid(form)

class BankingHallDesktopUpdateView(LoginRequiredMixin, UpdateView):

    model = BankingHallDesktop

    template_name = 'banking_hall_desktop_update.html'

    fields = ('cpu_serial_number', 'monitor_serial_number', 'keyboard_serial_number', 'description', 'floor_location')

    success_url = reverse_lazy('bankinghalldesktoptable')


class BankingHallDesktopDeleteView(LoginRequiredMixin,DeleteView):

    model = BankingHallDesktop

    template_name = 'banking_hall_desktop_delete.html'

    success_url = reverse_lazy('bankinghalldesktoptable')

    login_url = 'login'







class BankingHallBarcodeScannerListView(LoginRequiredMixin, ListView):

    model= BankingHallBarcodeScanner

    template_name= 'banking_hall_barcodescanner_table.html'

    context_object_name= 'banking_hall_barcodescanner_table'

    login_url = 'login'


class BankingHallBarcodeScannerDetailView(LoginRequiredMixin, DetailView):

    model= BankingHallBarcodeScanner

    template_name= 'banking_hall_barcodescanner_detail.html'

    login_url = 'login'




class BankingHallBarcodeScannerCreateView(LoginRequiredMixin, CreateView):

    model = BankingHallBarcodeScanner

    template_name = 'banking_hall_barcodescanner_create.html'

    fields = ('serial_number', 'type', 'description')

    success_url = reverse_lazy('bankinghallbarcodescannertable')

    login_url = 'login'


    def form_valid(self, form):

        form.instance.updated_by = self.request.user

        return super().form_valid(form)

class BankingHallBarcodeScannerUpdateView(LoginRequiredMixin, UpdateView):

    model = BankingHallBarcodeScanner

    template_name = 'banking_hall_barcodescanner_update.html'

    fields = ('serial_number', 'type', 'description')

    success_url = reverse_lazy('bankinghallbarcodescannertable')

    login_url = 'login'


class BankingHallBarcodeScannerDeleteView(LoginRequiredMixin,DeleteView):

    model = BankingHallBarcodeScanner

    template_name = 'banking_hall_barcodescanner_delete.html'

    success_url = reverse_lazy('bankinghallbarcodescannertable')

    login_url = 'login'
