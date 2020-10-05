from django.urls import path
from .views import ScannerListView


urlpatterns = [

    path('table/', ScannerListView.as_view(), name='scannertable'),
]
