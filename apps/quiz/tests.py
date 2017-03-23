from django.test import TestCase
from apps.quiz.models import Quiz
from apps.quiz.models import Question
from apps.quiz.models import Answer


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