from django.db import models

class Poll(models.Model):
    question = models.TextField(max_length=100)
    answer1 = models.TextField(max_length=100, default='')
    answer2 = models.TextField(max_length=100, default='')
    answer3 = models.TextField(max_length=100, blank=True, null=True)
    answer4 = models.TextField(max_length=100, blank=True, null=True)
    answer5 = models.TextField(max_length=100, blank=True, null=True)
    choice1 = models.IntegerField(default=0)
    choice2 = models.IntegerField(default=0)
    choice3 = models.IntegerField(default=0)
    choice4 = models.IntegerField(default=0)
    choice5 = models.IntegerField(default=0)

