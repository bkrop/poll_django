from django.db import models

class Poll(models.Model):
    question = models.TextField(max_length=100)
    choice1 = models.TextField(max_length=100)
    choice2 = models.TextField(max_length=100)
    choice3 = models.TextField(max_length=100, blank=True, null=True)
    choice4 = models.TextField(max_length=100, blank=True, null=True)
    choice5 = models.TextField(max_length=100, blank=True, null=True)
