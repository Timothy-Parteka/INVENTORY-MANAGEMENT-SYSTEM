from django.urls import path
from.views import FaultyListView

urlpatterns = [

    path('items/', FaultyListView.as_view(), name='faultyitems'),
]
