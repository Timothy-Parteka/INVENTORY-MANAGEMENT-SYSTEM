from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView

from .models import TenthFloorDataEntryDeskTop


# Create your views here.


#############CREATE VIEWS FOR LAND ADMIN DESKTOP#################
class TenthFloorDataEntryDesktopListView(LoginRequiredMixin,ListView):

    model = TenthFloorDataEntryDeskTop

    template_name = 'tenth_floor_dataentry_desktop_table.html'

    context_object_name = 'tenth_floor_dataentry_desktop'

    login_url = 'login'



class TenthFloorDataEntryDesktopDetailsView(LoginRequiredMixin,DetailView):

    model = TenthFloorDataEntryDeskTop

    template_name = 'tenth_floor_dataentry_desktop_details.html'

    login_url = 'login'


class TenthFloorDataEntryDesktopEditView(LoginRequiredMixin,UpdateView):

    model = TenthFloorDataEntryDeskTop

    template_name = 'tenth_floor_dataentry_desktop_edit.html'

    fields = ['cpu_serial_number', 'monitor_serial_number', 'keyboard_serial_number', 'description', 'floor_location']

    success_url = reverse_lazy('tenthfloordataentrydesktoptable')

    login_url = 'login'




class TenthFloorDataEntryDesktopCreateView(LoginRequiredMixin,CreateView):

    model = TenthFloorDataEntryDeskTop

    template_name = 'tenth_floor_dataentry_desktop_create.html'

    fields = ['cpu_serial_number', 'monitor_serial_number', 'keyboard_serial_number', 'description','floor_location']

    success_url = reverse_lazy('tenthfloordataentrydesktoptable')

    login_url = 'login'



    def form_valid(self, form):

        form.instance.updated_by = self.request.user

        return super().form_valid(form)


class TenthFloorDataEntryDesktopDeleteView(LoginRequiredMixin,DeleteView):

    model = TenthFloorDataEntryDeskTop

    template_name = 'tenth_floor_dataentry_desktop_delete.html'

    success_url = reverse_lazy('tenthfloordataentrydesktoptable')

    login_url = 'login'
