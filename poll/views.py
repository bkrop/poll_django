from django.shortcuts import render
from django.views.generic import CreateView
from .models import Poll

class PollCreateView(CreateView):
    model = Poll
    template_name = 'poll/create_poll.html'
    fields = ['question', 'choice1', 'choice2', 'choice3', 'choice4', 'choice5']

