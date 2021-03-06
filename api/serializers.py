from blog.models import Post
from polls.models import Poll, Vote
from django.db.models import Sum
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['author', 'title', 'text', 'created_date', 'published_date']

class PollSerializer(serializers.ModelSerializer):
    score = serializers.IntegerField()
    class Meta:
        model = Poll
        fields = ('title' ,'owner', 'score')

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ['voter', 'poll', 'value', 'vote_datetime']
