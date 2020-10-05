from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from thirdfloor.models import ThirdFloorDesktop
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

# Create your views here.

class ThirdFloorDesktopListView(LoginRequiredMixin, ListView):

    model= ThirdFloorDesktop

    template_name= 'third_floor_desktop_table.html'

    context_object_name= 'third_floor_desktop_table'

    login_url = 'login'


class ThirdFloorDesktopDetailView(LoginRequiredMixin, DetailView):

    model= ThirdFloorDesktop

    template_name= 'third_floor_desktop_detail.html'

    login_url = 'login'



class ThirdFloorDesktopCreateView(LoginRequiredMixin, CreateView):

    model = ThirdFloorDesktop

    template_name = 'third_floor_desktop_create.html'

    fields = ('cpu_serial_number', 'monitor_serial_number', 'keyboard_serial_number', 'description', 'floor_location')

    success_url = reverse_lazy('thirdfloordesktoptable')

    login_url = 'login'


    def form_valid(self, form):

        form.instance.updated_by = self.request.user

        return super().form_valid(form)

class ThirdFloorDesktopUpdateView(LoginRequiredMixin, UpdateView):

    model = ThirdFloorDesktop

    template_name = 'third_floor_desktop_update.html'

    fields = ('cpu_serial_number', 'monitor_serial_number', 'keyboard_serial_number', 'description', 'floor_location')

    success_url = reverse_lazy('thirdfloordesktoptable')

    login_url = 'login'



class ThirdFloorDesktopDeleteView(LoginRequiredMixin,DeleteView):

    model = ThirdFloorDesktop

    template_name = 'third_floor_desktop_delete.html'

    success_url = reverse_lazy('thirdfloordesktoptable')

    login_url = 'login'
