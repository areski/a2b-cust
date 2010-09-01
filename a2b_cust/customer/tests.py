import urllib, base64
from django.contrib.auth.models import User
from django.test import TestCase, Client
from a2b_cust.customer.models import Language

class LanguageTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('admin', 'admin@world.com', 'admin')
        self.user.is_staff = True
        self.user.is_superuser = True
        self.user.is_active = True
        self.user.save()
        auth = '%s:%s' % ('admin', 'admin')
        auth = 'Basic %s' % base64.encodestring(auth)
        auth = auth.strip()
        self.extra = {
            'HTTP_AUTHORIZATION': auth,            
        }
        self.dutch = Language.objects.create(code="Du", name="Dutch", lname="Dutch", charset="UTF-8")

    def language_get(self):
        response = self.client.get('/api/language', {}, **self.extra)
        self.assertEqual(response.status_code, 200)

    def language_put(self):
        response = self.client.put('/api/language/Du/', {'name': 'dutch'}, **self.extra)
        self.assertEqual(response.status_code, 200)
        
    def language_delete(self):
        response = self.client.delete('/api/language/Du/', {}, **self.extra)
        self.assertEqual(response.status_code, 204)

    def language_post(self):
        response = self.client.post('/api/language', { 'name':'Urdu' ,'code':'Ur','lname':'Urdu' ,'charset':'UTF-8'} , **self.extra)
        self.assertEqual(response.status_code, 200)