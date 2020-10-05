from django.urls import path
from messagingboard.views import MessagingboardListView, CommentCreateView


urlpatterns = [
    path('messageboard/', MessagingboardListView.as_view(), name='messageboard'),
    path('comment/', CommentCreateView.as_view(), name='comment')
]
