from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView

from .models import FourthFloorWingADeskTop


# Create your views here.


#############CREATE VIEWS FOR LAND ADMIN DESKTOP#################
class FourthFloorWingADesktopListView(LoginRequiredMixin,ListView):

    model = FourthFloorWingADeskTop

    template_name = 'fourth_floor_wingA_desktop_table.html'

    context_object_name = 'fourth_floor_wingA_desktop'

    login_url = 'login'



class FourthFloorWingADesktopDetailsView(LoginRequiredMixin,DetailView):

    model = FourthFloorWingADeskTop

    template_name = 'fourth_floor_wingA_desktop_details.html'

    login_url = 'login'


class FourthFloorWingADesktopEditView(LoginRequiredMixin,UpdateView):

    model = FourthFloorWingADeskTop

    template_name = 'fourth_floor_wingA_desktop_edit.html'

    fields = ['cpu_serial_number', 'monitor_serial_number', 'keyboard_serial_number', 'description', 'floor_location']

    success_url = reverse_lazy('fourthfloorwingadesktoptable')

    login_url = 'login'




class FourthFloorWingADesktopCreateView(LoginRequiredMixin,CreateView):

    model = FourthFloorWingADeskTop

    template_name = 'fourth_floor_wingA_desktop_create.html'

    fields = ['cpu_serial_number', 'monitor_serial_number', 'keyboard_serial_number', 'description', 'floor_location']

    success_url = reverse_lazy('fourthfloorwingadesktoptable')

    login_url = 'login'



    def form_valid(self, form):

        form.instance.updated_by = self.request.user

        return super().form_valid(form)


class FourthFloorWingADesktopDeleteView(LoginRequiredMixin,DeleteView):

    model = FourthFloorWingADeskTop

    template_name = 'fourth_floor_wingA_desktop_delete.html'

    success_url = reverse_lazy('fourthfloorwingadesktoptable')

    login_url = 'login'
