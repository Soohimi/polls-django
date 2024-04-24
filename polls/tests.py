from django.test import TestCase
from django.utils import timezone
from .models import Question

import datetime

class QuestionModelTests(TestCase):

    #was_published_recently() must return false for future questions
    def test_was_published_recently(self):
        time = timezone.now() + datetime.timedelta(days=10)
        future_question = Question(publish_date=time)
        self.assertIs(future_question.was_published_recently,False)

