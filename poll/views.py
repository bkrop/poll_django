from django.shortcuts import render
from django.views.generic import CreateView
from .models import Poll
from .forms import VoteForm

class PollCreateView(CreateView):
    model = Poll
    template_name = 'poll/create_poll.html'
    fields = ['question', 'answer1', 'answer2', 'answer3', 'answer4', 'answer5']

def vote(request, poll_pk):
    poll = Poll.objects.get(pk=poll_pk)
    if request.method == 'POST':
        selected_option = request.POST['poll']
        print(selected_option)
        if selected_option == 'answer1':
            poll.choice1 += 1
        poll.save()
    context = {
        'poll': poll
    }
    return render(request, 'poll/vote.html', context=context)

