from django.urls import path
from .views import OrderItemList


urlpatterns = [

    path('', OrderItemList.as_view(), name='orderitem'),
]
