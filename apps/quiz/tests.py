from django.test import TestCase
from django.test import Client
from apps.quiz.models import Quiz
from apps.quiz.models import Question
from apps.quiz.models import Answer
from django.urls import reverse
from django.template import Context, Template
import unittest

#Model tests
#View tests

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


#Template tags tests
class TemplateTagTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.get_url = lambda w, h, fmt: reverse(
                            'dummyimage.views.render_image',
                            args=(w, h, fmt))

    def get_template(self, arguments):
        return '{%% load quiz_tags %%}{%% get_dummyimage_url %s %%}' % arguments

    def test_render_filename(self):
        url = self.get_url(100, 100, 'jpg')
        t = Template(self.get_template('100x100.jpg'))
        c = Context({})
        self.failUnlessEqual(url, t.render(c))
