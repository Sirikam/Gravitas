from django.test import TestCase

# Create your tests here.

class YourTestClass(TestCase):

    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        pass

    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass

#GET or POST by anonymous user (should redirect to login page)
#GET or POST by logged-in user with no profile (should raise a UserProfile.DoesNotExist exception)
#GET by logged-in user (should show the form)
#POST by logged-in user with blank data (should show form errors)
#POST by logged-in user with invalid data (should show form errors)
#POST by logged-in user with valid data (should redirect)

    def test_call_view_denies_anonymous(self):
        response = self.client.get('/url/to/view', follow=True)
        self.assertRedirects(response, '/login/')
        response = self.client.post('/url/to/view', follow=True)
        self.assertRedirects(response, '/login/')

    def test_call_view_loads(self):
        self.client.login(username='user', password='test')  # defined in fixture or with factory in setUp()
        response = self.client.get('/url/to/view')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'conversation.html')

    def test_call_view_fails_blank(self):
        self.client.login(username='user', password='test')
        response = self.client.post('/url/to/view', {})  # blank data dictionary
        self.assertFormError(response, 'form', 'some_field', 'This field is required.')
        # etc. ...

    def test_call_view_fails_invalid(self):

    # as above, but with invalid rather than blank data in dictionary

    def test_call_view_fails_invalid(self):
        # same again, but with valid data, then
        self.assertRedirects(response, '/contact/1/calls/')
