from django.urls import path
from.views import StockInListView

urlpatterns = [

    path('', StockInListView.as_view(), name='stockin'),
]
