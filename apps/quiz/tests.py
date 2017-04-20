from django.test import TestCase
from apps.quiz.models import Quiz
from apps.quiz.models import Question
from apps.quiz.models import Answer
from django.urls import reverse


class QuizTest(TestCase):

    def test_quiz(self):
        quiz_instance = Quiz(quiz_navn="quiznavn")
        self.assertEqual(quiz_instance.__str__(), 'quiznavn')

    def test_question(self):
        question_instance = Question(spoersmaal_stilt="spørsmal")
        self.assertEqual(question_instance.__str__(), 'spørsmal')

    def test_answer(self):
        answer_instance = Answer(answer_alt="svar")
        self.assertEqual(answer_instance.__str__(), 'svar')

class QuizViewTest(TestCase):
    def test_index(self):
        response = self.client.get(reverse('quiz:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No quizzes are available")