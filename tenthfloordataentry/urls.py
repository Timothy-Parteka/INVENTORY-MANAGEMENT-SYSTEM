from django.urls import path

from .views import TenthFloorDataEntryDesktopListView,TenthFloorDataEntryDesktopDetailsView,TenthFloorDataEntryDesktopCreateView,TenthFloorDataEntryDesktopEditView,TenthFloorDataEntryDesktopDeleteView


urlpatterns = [
    path('desktoptable/',TenthFloorDataEntryDesktopListView.as_view(), name='tenthfloordataentrydesktoptable'),
    path('desktopdetail/<int:pk>/',TenthFloorDataEntryDesktopDetailsView.as_view(), name='tenthfloordataentrydesktopdetails'),
    path('desktopcreate/',TenthFloorDataEntryDesktopCreateView.as_view(), name='tenthfloordataentrydesktopcreate'),
    path('desktopedit/<int:pk>/',TenthFloorDataEntryDesktopEditView.as_view(), name='tenthfloordataentrydesktopedit'),
    path('desktopdelete/<int:pk>/',TenthFloorDataEntryDesktopDeleteView.as_view(), name='tenthfloordataentrydesktopdelete'),
]
