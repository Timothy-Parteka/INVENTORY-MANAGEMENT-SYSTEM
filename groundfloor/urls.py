from django.urls import path

from .views import GroundFloorDesktopListView,GroundFloorDesktopDetailsView,GroundFloorDesktopCreateView,GroundFloorDesktopEditView,GroundFloorDesktopDeleteView


urlpatterns = [
    path('desktoptable/',GroundFloorDesktopListView.as_view(), name='groundfloordesktoptable'),
    path('desktopdetail/<int:pk>/',GroundFloorDesktopDetailsView.as_view(), name='groundfloordesktopdetail'),
    path('desktopcreate/',GroundFloorDesktopCreateView.as_view(), name='groundfloordesktopcreate'),
    path('desktopedit/<int:pk>/',GroundFloorDesktopEditView.as_view(), name='groundfloordesktopedit'),
    path('desktopdelete/<int:pk>/',GroundFloorDesktopDeleteView.as_view(), name='groundfloordesktopdelete'),

]
