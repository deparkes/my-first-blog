from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Poll(models.Model):
    title = models.CharField(max_length=30)
    owner = models.CharField(max_length=30)
    
    def __str__(self):
        return self.title

class Vote(models.Model):
    voter = models.CharField(max_length=30)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    vote_datetime = models.DateTimeField('time voted')
    CHOICES = [(-1, "Down"), (1, "Up")]
    value = models.IntegerField(choices=CHOICES)

