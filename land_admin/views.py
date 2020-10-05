from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView

from .models import LandAdminDeskTop, LandAdminBarCodeScanner


# Create your views here.


#############CREATE VIEWS FOR LAND ADMIN DESKTOP#################
class LandAdminDeskTopList(LoginRequiredMixin,ListView):

    model = LandAdminDeskTop

    template_name = 'land_admin_desktop_table.html'

    context_object_name = 'desktoptable'

    login_url = 'login'



class LandAdminDeskTopDetails(LoginRequiredMixin,DetailView):

    model = LandAdminDeskTop

    template_name = 'land_admin_desktop_details.html'

    login_url = 'login'


class LandAdminDeskTopEdit(LoginRequiredMixin,UpdateView):

    model = LandAdminDeskTop

    template_name = 'land_admin_desktop_edit.html'

    fields = ['cpu_serial_number', 'monitor_serial_number', 'keyboard_serial_number', 'description', 'floor_location']

    success_url = reverse_lazy('landadmindesktoplist')

    login_url = 'login'




class LandAdminDesktopCreate(LoginRequiredMixin,CreateView):

    model = LandAdminDeskTop

    template_name = 'land_admin_desktop_create.html'

    fields = ['cpu_serial_number', 'monitor_serial_number', 'keyboard_serial_number', 'description', 'floor_location']

    success_url = reverse_lazy('landadmindesktoplist')

    login_url = 'login'



    def form_valid(self, form):

        form.instance.updated_by = self.request.user

        return super().form_valid(form)


class LandAdminDesktopDelete(LoginRequiredMixin,DeleteView):

    model = LandAdminDeskTop

    template_name = 'land_admin_desktop_delete.html'

    success_url = reverse_lazy('landadmindesktoplist')

    login_url = 'login'




###########END LAND ADMIN DESKTOP VIEW#############



###########CREATE LAND ADMIN BARCODE SCANNER VIEW##########

class LandAdminBarCodeScannerList(ListView):

    model = LandAdminBarCodeScanner

    template_name = 'land_admin_barcodescanner_table.html'

    context_object_name = 'barcodescanner_list'

    login_url = 'login'



class LandAdminBarCodeScannerDetails(DetailView):

    model = LandAdminBarCodeScanner

    template_name = 'land_admin_barcodescanner_details.html'

    login_url = 'login'


class LandAdminBarCodeScannerEdit(UpdateView):

    model = LandAdminBarCodeScanner

    template_name = 'land_admin_barcodescanner_edit.html'

    fields = ['serial_number', 'type', 'description',]

    success_url = reverse_lazy('landadminbarcodescannerlist')

    login_url = 'login'




class LandAdminBarCodeScannerCreate(CreateView):

    model = LandAdminBarCodeScanner

    template_name = 'land_admin_barcodescanner_create.html'

    fields = ['serial_number', 'type', 'description',]

    success_url = reverse_lazy('landadminbarcodescannerlist')

    login_url = 'login'



    def form_valid(self, form):

        form.instance.updated_by = self.request.user

        return super().form_valid(form)


class LandAdminBarCodeScannerDelete(DeleteView):

    model = LandAdminBarCodeScanner

    template_name = 'land_admin_barcodescanner_delete.html'

    success_url = reverse_lazy('landadminbarcodescannerlist')

    login_url = 'login'
