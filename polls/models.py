import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    publish_date = models.DateTimeField("date published")

    def __str__(self):
        return 'Question==' + self.question_text + ' | Date==' + self.publish_date.strftime("%m/%d/%Y, %H:%M:%S")

    @admin.display(
        boolean=True,
        ordering="publish_date",
        description="Published recently?",
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.publish_date <= now
    
    


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return 'Choice==' + self.choice + ' | Votes==' + str(self.votes)
