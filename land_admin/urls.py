from django.urls import path
from .views import (

    LandAdminDeskTopList,
    LandAdminDeskTopDetails,
    LandAdminDeskTopEdit,
    LandAdminDesktopCreate,
    LandAdminDesktopDelete,
    LandAdminBarCodeScannerList,
    LandAdminBarCodeScannerDetails,
    LandAdminBarCodeScannerEdit,
    LandAdminBarCodeScannerCreate,
    LandAdminBarCodeScannerDelete,

)



urlpatterns = [

    path('desktop/', LandAdminDeskTopList.as_view(), name= 'landadmindesktoplist'),
    path('<int:pk>/', LandAdminDeskTopDetails.as_view(), name= 'landadmindesktopdetails'),
    path('landadmindesktop/<int:pk>edit/', LandAdminDeskTopEdit.as_view(), name= 'landadmindesktopedit'),
    path('landadmindesktopcreate/', LandAdminDesktopCreate.as_view(), name= 'landadmindesktopcreate'),
    path('<int:pk>/delete/', LandAdminDesktopDelete.as_view(), name= 'landadmindesktopdelete'),
    path('barcodescanner/', LandAdminBarCodeScannerList.as_view(), name= 'landadminbarcodescannerlist'),
    path('barcodescanner/<int:pk>details/', LandAdminBarCodeScannerDetails.as_view(), name= 'landadminbarcodescannerdetails'),
    path('barcodescanner/<int:pk>edit/', LandAdminBarCodeScannerEdit.as_view(), name= 'landadminbarcodescanneredit'),
    path('barcodescannercreate/', LandAdminBarCodeScannerCreate.as_view(), name= 'landadminbarcodescannercreate'),
    path('barcodescanner<int:pk>/delete/', LandAdminBarCodeScannerDelete.as_view(), name= 'landadminbarcodescannerdelete'),
]
