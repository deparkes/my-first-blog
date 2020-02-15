from blog.models import Post
from polls.models import Poll, Vote
from rest_framework import viewsets
from api.serializers import PostSerializer, PollSerializer, VoteSerializer
from django.db.models import Sum

class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows posts to be viewed or edited.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PollViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows polls to be viewed or edited.
    """
    queryset = Poll.objects.all()
    serializer_class = PollSerializer

    def get_queryset(self):
        return Poll.objects.annotate(score=Sum('vote__value'))


class VoteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows votes to be viewed or edited.
    """
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer