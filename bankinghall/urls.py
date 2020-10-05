from django.urls import path

from .views import (

    BankingHallDesktopListView,
    BankingHallDesktopDetailView,
    BankingHallDesktopCreateView,
    BankingHallDesktopUpdateView,
    BankingHallDesktopDeleteView,
    BankingHallBarcodeScannerListView,
    BankingHallBarcodeScannerDetailView,
    BankingHallBarcodeScannerCreateView,
    BankingHallBarcodeScannerUpdateView,
    BankingHallBarcodeScannerDeleteView,
)

urlpatterns = [
    path('desktop/', BankingHallDesktopListView.as_view(), name='bankinghalldesktoptable'),
    path('desktopdetail/<int:pk>/', BankingHallDesktopDetailView.as_view(), name='bankinghalldesktopdetail'),
    path('desktopcreate/', BankingHallDesktopCreateView.as_view(), name='bankinghalldesktopcreate'),
    path('desktopupdate/<int:pk>/', BankingHallDesktopUpdateView.as_view(), name='bankinghalldesktopupdate'),
    path('desktopdelete/<int:pk>/', BankingHallDesktopDeleteView.as_view(), name='bankinghalldesktopdelete'),
    path('barcodescannertable/', BankingHallBarcodeScannerListView.as_view(), name='bankinghallbarcodescannertable'),
    path('barcodescannerdetail/<int:pk>/', BankingHallBarcodeScannerDetailView.as_view(), name='bankinghallbarcodescannerdetail'),
    path('barcodescannercreate/', BankingHallBarcodeScannerCreateView.as_view(), name='bankinghallbarcodescannercreate'),
    path('barcodescannerupdate/<int:pk>/', BankingHallBarcodeScannerUpdateView.as_view(), name='bankinghallbarcodescannerupdate'),
    path('barcodescannerdelete/<int:pk>/', BankingHallBarcodeScannerDeleteView.as_view(), name='bankinghallbarcodescannerdelete'),


]
