from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView

from .models import GroundFloorDeskTop


# Create your views here.


#############CREATE VIEWS FOR LAND ADMIN DESKTOP#################
class GroundFloorDesktopListView(LoginRequiredMixin,ListView):

    model = GroundFloorDeskTop

    template_name = 'ground_floor_desktop_table.html'

    context_object_name = 'ground_floor_desktop'

    login_url = 'login'



class GroundFloorDesktopDetailsView(LoginRequiredMixin,DetailView):

    model = GroundFloorDeskTop

    template_name = 'ground_floor_desktop_details.html'

    login_url = 'login'


class GroundFloorDesktopEditView(LoginRequiredMixin,UpdateView):

    model = GroundFloorDeskTop

    template_name = 'ground_floor_desktop_edit.html'

    fields = ['cpu_serial_number', 'monitor_serial_number', 'keyboard_serial_number', 'description', 'floor_location']

    success_url = reverse_lazy('groundfloordesktoptable')

    login_url = 'login'




class GroundFloorDesktopCreateView(LoginRequiredMixin,CreateView):

    model = GroundFloorDeskTop

    template_name = 'ground_floor_desktop_create.html'

    fields = ['cpu_serial_number', 'monitor_serial_number', 'keyboard_serial_number', 'description', 'floor_location']

    success_url = reverse_lazy('groundfloordesktoptable')

    login_url = 'login'



    def form_valid(self, form):

        form.instance.updated_by = self.request.user

        return super().form_valid(form)


class GroundFloorDesktopDeleteView(LoginRequiredMixin,DeleteView):

    model = GroundFloorDeskTop

    template_name = 'ground_floor_desktop_delete.html'

    success_url = reverse_lazy('groundfloordesktoptable')

    login_url = 'login'
