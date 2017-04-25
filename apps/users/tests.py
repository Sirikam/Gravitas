import inspect

from django.core.urlresolvers import resolve, reverse
from django.test import TestCase
from .forms import *


"""class User_Form_Test(TestCase):

    def setUp(self):
        self.person = Person.objects.create(email="admin@grav.com", password="gravitas", first_name="admin",
                                            phone=12345678, PERSON_ROLE="ST")
    # Valid Form Data
    def test_PersonForm_valid(self):
        form = PersonForm(data={'email': "admin@grav.com", 'password': "gravitas",
                                'first_name': "admin", 'phone': 12345678, 'PERSON_ROLE': "professor"})
        self.assertTrue(form.is_valid())
"""

