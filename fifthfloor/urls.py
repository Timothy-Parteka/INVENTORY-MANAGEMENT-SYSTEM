from django.urls import path

from .views import FifthFloorDesktopListView,FifthFloorDesktopDetailView,FifthFloorDesktopCreateView,FifthFloorDesktopUpdateView,FifthFloorDesktopDeleteView


urlpatterns = [
    path('desktoptable/',FifthFloorDesktopListView.as_view(), name='fifthfloordesktoptable'),
    path('desktopdetail/<int:pk>/',FifthFloorDesktopDetailView.as_view(), name='fifthfloordesktopdetail'),
    path('desktopcreate/',FifthFloorDesktopCreateView.as_view(), name='fifthfloordesktopcreate'),
    path('desktopedit/<int:pk>/',FifthFloorDesktopUpdateView.as_view(), name='fifthfloordesktopupdate'),
    path('desktopdelete/<int:pk>/',FifthFloorDesktopDeleteView.as_view(), name='fifthfloordesktopdelete'),

]
