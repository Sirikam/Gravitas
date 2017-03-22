from unittest import TestCase
from django.test import TestCase, RequestFactory

from django.http import HttpResponse
from django.http import response
from django.test import Client
from apps import staticpages
#from views import StaticView


c = Client()
c.get('/staticpages/')


class GreetingsTest(TestCase):

    def test_greeting(self):
        self.assertRaises(Exception)
       # self.assertContains(response, "New<br></br>Lines", count=None, status_code=202, msg_prefix='', html=True)
        self.assertHTMLEqual("<h1>welcome<\h1>", "<h1>welcome<\h1>", msg='')

   # def test_get(self):
