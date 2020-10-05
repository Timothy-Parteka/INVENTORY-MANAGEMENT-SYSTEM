from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import FifthFloorDesktop
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

# Create your views here.

class FifthFloorDesktopListView(LoginRequiredMixin, ListView):

    model= FifthFloorDesktop

    template_name= 'fifth_floor_desktop_table.html'

    context_object_name= 'fifth_floor_desktop'

    login_url = 'login'


class FifthFloorDesktopDetailView(LoginRequiredMixin, DetailView):

    model= FifthFloorDesktop

    template_name= 'fifth_floor_desktop_detail.html'

    login_url = 'login'



class FifthFloorDesktopCreateView(LoginRequiredMixin, CreateView):

    model = FifthFloorDesktop

    template_name = 'fifth_floor_desktop_create.html'

    fields = ('cpu_serial_number', 'monitor_serial_number', 'keyboard_serial_number', 'description', 'floor_location')

    success_url = reverse_lazy('fifthfloordesktoptable')

    login_url = 'login'


    def form_valid(self, form):

        form.instance.updated_by = self.request.user

        return super().form_valid(form)

class FifthFloorDesktopUpdateView(LoginRequiredMixin, UpdateView):

    model = FifthFloorDesktop

    template_name = 'fifth_floor_desktop_update.html'

    fields = ('cpu_serial_number', 'monitor_serial_number', 'keyboard_serial_number', 'description', 'floor_location')

    success_url = reverse_lazy('fifthfloordesktoptable')

    login_url = 'login'



class FifthFloorDesktopDeleteView(LoginRequiredMixin,DeleteView):

    model = FifthFloorDesktop

    template_name = 'fifth_floor_desktop_delete.html'

    success_url = reverse_lazy('fifthfloordesktoptable')

    login_url = 'login'
