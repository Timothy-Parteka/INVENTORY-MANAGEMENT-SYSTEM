from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from messagingboard.models import Messagingboard, Comment
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy


# Create your views here.

class MessagingboardListView(LoginRequiredMixin,ListView):
    model = Messagingboard
    template_name = 'message_board.html'
    login_url = 'login'


class CommentCreateView(LoginRequiredMixin,CreateView):
    model = Comment
    template_name = 'comment_create.html'
    fields = ['message', 'comment']
    success_url = reverse_lazy('messageboard')
    login_url = 'login'

    def form_valid(self, form):

        form.instance.comment_by = self.request.user

        return super().form_valid(form)
