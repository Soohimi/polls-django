from django.test import TestCase
from django.utils import timezone
from .models import Question
from django.urls import reverse

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

def create_question(question_text, days):
    #Creates a question 
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, publish_date=time)

class QuestionIndexViewTests(TestCase):
    #Test case for scenarios where no questions exist and an appropriate message must be shown.
    def test_no_questions(self):
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code,200)
        self.assertContains(response,"No polls are available.")
        self.assertQuerySetEqual(response.context["question_list"],[])

    #Test case for scenarios where past questions exist and they must be displayed.
    def test_past_question(self):
        question = create_question(question_text="Past question.", days=-30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(response.context["question_list"],[question])

    #Test case for scenarios where future questions exist and they should not be displayed.
    def test_future_question(self):
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertContains(response, "No polls are available.")
        self.assertQuerySetEqual(response.context["question_list"],[])

    #Test case for scenarios where both past and future questions exist and only the past ones should be displayed
    def test_future_and_past_question(self):
        question = create_question(question_text="Past question.", days=-30)
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["question_list"],
            [question],
        )

    #Test case for more than one questions to be displayed    
    def test_two_past_questions(self):
        question1 = create_question(question_text="First past question.", days=-30)
        question2 = create_question(question_text="Second past question.", days=-5)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["question_list"],
            [question2, question1],
        )

        
