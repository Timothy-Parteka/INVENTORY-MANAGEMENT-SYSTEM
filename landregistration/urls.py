from django.urls import path
from .views import LandRegDeskTopList,LandRegDeskTopDetails,LandRegDeskTopEdit,LandRegDeskTopCreate,LandRegDeskTopDelete



urlpatterns = [

    path('desktop/', LandRegDeskTopList.as_view(), name= 'landregdesktoptable'),
    path('<int:pk>/', LandRegDeskTopDetails.as_view(), name= 'landregdesktopdetails'),
    path('landregdesktop/<int:pk>edit/', LandRegDeskTopEdit.as_view(), name= 'landregdesktopedit'),
    path('landregdesktopcreate/', LandRegDeskTopCreate.as_view(), name= 'landregdesktopcreate'),
    path('<int:pk>/delete/', LandRegDeskTopDelete.as_view(), name= 'landregdesktopdelete'),

]
