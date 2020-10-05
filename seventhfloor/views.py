from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView

from .models import SeventhFloorDeskTop




#############CREATE VIEWS FOR SEVENTH FLOOR DESKTOP#################
class SeventhFloorDeskTopList(LoginRequiredMixin,ListView):

    model = SeventhFloorDeskTop

    template_name = 'seventh_floor_desktop_table.html'

    context_object_name = 'desktoptable'

    login_url = 'login'



class SeventhFloorDeskTopDetails(LoginRequiredMixin,DetailView):

    model = SeventhFloorDeskTop

    template_name = 'seventh_floor_desktop_details.html'

    login_url = 'login'


class SeventhFloorDeskTopEdit(LoginRequiredMixin,UpdateView):

    model = SeventhFloorDeskTop

    template_name = 'seventh_floor_desktop_edit.html'

    fields = ['cpu_serial_number', 'monitor_serial_number', 'keyboard_serial_number', 'description', 'floor_location']

    success_url = reverse_lazy('seventhfloordesktoplist')

    login_url = 'login'



class SeventhFloorDesktopCreate(LoginRequiredMixin,CreateView):

    model = SeventhFloorDeskTop

    template_name = 'seventh_floor_desktop_create.html'

    fields = ['cpu_serial_number', 'monitor_serial_number', 'keyboard_serial_number', 'description', 'floor_location']

    success_url = reverse_lazy('seventhfloordesktoplist')

    login_url = 'login'


    def form_valid(self, form):

        form.instance.updated_by = self.request.user

        return super().form_valid(form)


class SeventhFloorDesktopDelete(LoginRequiredMixin,DeleteView):

    model = SeventhFloorDeskTop

    template_name = 'seventh_floor_desktop_delete.html'

    success_url = reverse_lazy('seventhfloordesktoplist')

    login_url = 'login'
