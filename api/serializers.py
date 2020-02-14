from blog.models import Post
from polls.models import Poll
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['author', 'title', 'text', 'created_date', 'published_date']


class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = ['title' ,'owner']
