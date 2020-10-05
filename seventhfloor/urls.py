from django.urls import path
from .views import (

    SeventhFloorDeskTopList,
    SeventhFloorDeskTopDetails,
    SeventhFloorDeskTopEdit,
    SeventhFloorDesktopCreate,
    SeventhFloorDesktopDelete,

)



urlpatterns = [

    path('desktop/', SeventhFloorDeskTopList.as_view(), name= 'seventhfloordesktoplist'),
    path('desktop/<int:pk>details/', SeventhFloorDeskTopDetails.as_view(), name= 'seventhfloordesktopdetails'),
    path('desktop/<int:pk>edit/', SeventhFloorDeskTopEdit.as_view(), name= 'seventhfloordesktopedit'),
    path('desktopcreate/', SeventhFloorDesktopCreate.as_view(), name= 'seventhfloordesktopcreate'),
    path('<int:pk>/delete/', SeventhFloorDesktopDelete.as_view(), name= 'seventhfloordesktopdelete'),
]
