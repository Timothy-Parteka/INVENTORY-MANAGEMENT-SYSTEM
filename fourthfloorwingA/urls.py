from django.urls import path

from fourthfloorwingA.views import FourthFloorWingADesktopListView,FourthFloorWingADesktopDetailsView,FourthFloorWingADesktopCreateView,FourthFloorWingADesktopEditView,FourthFloorWingADesktopDeleteView


urlpatterns = [
    path('desktoptable/',FourthFloorWingADesktopListView.as_view(), name='fourthfloorwingadesktoptable'),
    path('desktopdetail/<int:pk>/',FourthFloorWingADesktopDetailsView.as_view(), name='fourthfloorwingadesktopdetails'),
    path('desktopcreate/',FourthFloorWingADesktopCreateView.as_view(), name='fourthfloorwingadesktopcreate'),
    path('desktopedit/<int:pk>/',FourthFloorWingADesktopEditView.as_view(), name='fourthfloorwingadesktopedit'),
    path('desktopdelete/<int:pk>/',FourthFloorWingADesktopDeleteView.as_view(), name='fourthfloorwingadesktopdelete'),
]
