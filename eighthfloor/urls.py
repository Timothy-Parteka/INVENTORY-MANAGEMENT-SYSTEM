from django.urls import path

from .views import EighthFloorDesktopListView,EighthFloorDesktopDetailsView,EighthFloorDesktopCreateView,EighthFloorDesktopEditView,EighthFloorDesktopDeleteView


urlpatterns = [
    path('desktoptable/',EighthFloorDesktopListView.as_view(), name='eighthfloordesktoptable'),
    path('desktopdetail/<int:pk>/',EighthFloorDesktopDetailsView.as_view(), name='eighthfloordesktopdetail'),
    path('desktopcreate/',EighthFloorDesktopCreateView.as_view(), name='eighthfloordesktopcreate'),
    path('desktopedit/<int:pk>/',EighthFloorDesktopEditView.as_view(), name='eighthfloordesktopedit'),
    path('desktopdelete/<int:pk>/',EighthFloorDesktopDeleteView.as_view(), name='eighthfloordesktopdelete'),

]
