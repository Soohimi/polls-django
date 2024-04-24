from django.test import TestCase
from django.utils import timezone
from .models import Question

import datetime

class QuestionModelTests(TestCase):

    #was_published_recently() must return false for future questions.
    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=10)
        future_question = Question(publish_date=time)
        self.assertIs(future_question.was_published_recently,False)

    #was_published_recently() must return false for questions with publish_date older than 1 day. 
    def test_was_published_recently_with_old_question(self):
        time = timezone.now() - datetime.timedelta(days=1 , seconds=1)
        old_question = Question(publish_date=time)
        self.assertIs(old_question.was_published_recently,False)
    #was_published_recently() must return true for questions with publish_date within the last day.    
    def test_was_published_recently_with_recent_question(self):
        time=timezone.now() - datetime.timedelta(hours=23,minutes=59,seconds=59,milliseconds=999)
        recent_question = Question(publish_date=time)
        self.assertIs(recent_question.was_published_recently,True)
