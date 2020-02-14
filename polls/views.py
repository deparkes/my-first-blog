from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import Sum
from django.utils import timezone
from .models import Poll, Vote
# Create your views here.

def index(request):
    available_polls = Poll.objects.all()
    context = {'available_polls': available_polls}
    return render(request, 'polls/index.html', context)

def detail(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/detail.html', {'poll': poll})

def results(request, poll_id):
    aggregate = Poll.objects.aggregate(score=Sum('vote__value'))
    return HttpResponse("Current score: " + str(aggregate['score']))

def vote(request, poll_id, vote_choice):
    poll = get_object_or_404(Poll, pk=poll_id)
    CHOICES = {'up': 1, 'down': -1}
    v = Vote(voter=request.user, poll=poll, vote_datetime=timezone.now(), value=CHOICES[vote_choice])
    v.save()
    return HttpResponse("You're voting on poll %s." % poll_id)
