from django.urls import path

from thirdfloor.views import ThirdFloorDesktopListView,ThirdFloorDesktopDetailView,ThirdFloorDesktopCreateView,ThirdFloorDesktopUpdateView,ThirdFloorDesktopDeleteView


urlpatterns = [
    path('desktoptable/',ThirdFloorDesktopListView.as_view(), name='thirdfloordesktoptable'),
    path('desktopdetail/<int:pk>/',ThirdFloorDesktopDetailView.as_view(), name='thirdfloordesktopdetail'),
    path('desktopcreate/',ThirdFloorDesktopCreateView.as_view(), name='thirdfloordesktopcreate'),
    path('desktopupdate/<int:pk>/',ThirdFloorDesktopUpdateView.as_view(), name='thirdfloordesktopupdate'),
    path('desktopdelete/<int:pk>/',ThirdFloorDesktopDeleteView.as_view(), name='thirdfloordesktopdelete'),

]
