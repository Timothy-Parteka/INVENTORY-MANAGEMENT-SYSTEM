from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from .models import LandRegDeskTop



# Create your views here.


#############CREATE VIEWS FOR LAND ADMIN DESKTOP#################
class LandRegDeskTopList(LoginRequiredMixin,ListView):

    model = LandRegDeskTop

    template_name = 'land_reg_desktop_table.html'

    context_object_name = 'land_reg_desktop'

    login_url = 'login'



class LandRegDeskTopDetails(LoginRequiredMixin,DetailView):

    model = LandRegDeskTop

    template_name = 'land_reg_desktop_details.html'

    login_url = 'login'


class LandRegDeskTopEdit(LoginRequiredMixin,UpdateView):

    model = LandRegDeskTop

    template_name = 'land_reg_desktop_edit.html'

    fields = ['cpu_serial_number', 'monitor_serial_number', 'keyboard_serial_number', 'description', 'floor_location']

    success_url = reverse_lazy('landregdesktoptable')

    login_url = 'login'




class LandRegDeskTopCreate(LoginRequiredMixin,CreateView):

    model = LandRegDeskTop

    template_name = 'land_reg_desktop_create.html'

    fields = ['cpu_serial_number', 'monitor_serial_number', 'keyboard_serial_number', 'description', 'floor_location']

    success_url = reverse_lazy('landregdesktoptable')

    login_url = 'login'



    def form_valid(self, form):

        form.instance.updated_by = self.request.user

        return super().form_valid(form)


class LandRegDeskTopDelete(LoginRequiredMixin,DeleteView):

    model = LandRegDeskTop

    template_name = 'land_reg_desktop_delete.html'

    success_url = reverse_lazy('landregdesktoptable')

    login_url = 'login'
