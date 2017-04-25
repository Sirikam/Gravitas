import inspect

from django.core.urlresolvers import resolve, reverse
from django.test import TestCase
from .forms import *
from django.test import Client


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

class PersonTest(TestCase):
    def setUp(self):
        self.ole = Person.objects.create(first_name='Ole', last_name='Nordmann', middle_name=' ', PERSON_ROLE='ST')
        self.kari = Person.objects.create(first_name='Kari', last_name='Nordmann', middle_name=' ', PERSON_ROLE='ST')

    def test_kari_first_name(self):
        self.assertEqual(self.alice.first_name, 'Kari')

    def test_ole_first_name(self):
        self.assertEqual(self.bob.first_name, 'Ole')

    def test_ole_first_name_modified(self):
        self.ole.first_name = 'Truls'
        self.ole.save()
        self.assertEqual(self.ole.first_name, 'Truls')
