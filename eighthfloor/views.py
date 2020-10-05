from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView

from .models import EighthFloorDeskTop


# Create your views here.


#############CREATE VIEWS FOR LAND ADMIN DESKTOP#################
class EighthFloorDesktopListView(LoginRequiredMixin,ListView):

    model = EighthFloorDeskTop

    template_name = 'eighth_floor_desktop_table.html'

    context_object_name = 'eighth_floor_desktop'

    login_url = 'login'



class EighthFloorDesktopDetailsView(LoginRequiredMixin,DetailView):

    model = EighthFloorDeskTop

    template_name = 'eighth_floor_desktop_details.html'

    login_url = 'login'


class EighthFloorDesktopEditView(LoginRequiredMixin,UpdateView):

    model = EighthFloorDeskTop

    template_name = 'eighth_floor_desktop_edit.html'

    fields = ['cpu_serial_number', 'monitor_serial_number', 'keyboard_serial_number', 'description', 'floor_location']

    success_url = reverse_lazy('eighthfloordesktoptable')

    login_url = 'login'




class EighthFloorDesktopCreateView(LoginRequiredMixin,CreateView):

    model = EighthFloorDeskTop

    template_name = 'eighth_floor_desktop_create.html'

    fields = ['cpu_serial_number', 'monitor_serial_number', 'keyboard_serial_number', 'description', 'floor_location']

    success_url = reverse_lazy('eighthfloordesktoptable')

    login_url = 'login'



    def form_valid(self, form):

        form.instance.updated_by = self.request.user

        return super().form_valid(form)


class EighthFloorDesktopDeleteView(LoginRequiredMixin,DeleteView):

    model = EighthFloorDeskTop

    template_name = 'eighth_floor_desktop_delete.html'

    success_url = reverse_lazy('eighthfloordesktoptable')

    login_url = 'login'
