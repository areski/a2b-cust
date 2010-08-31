import urllib, base64
from django.contrib.auth.models import User
from django.test import TestCase, Client
from a2b_cust.customer.models import Language
from function_def import my_func


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
            'HTTP_X_REQUESTED_WITH':'XMLHttpRequest'
        }
        self.dutch = Language.objects.create(code="Du", name="Dutch", lname="Dutch", charset="UTF-8")

    def test_get(self):
        response = self.client.get('/api/language', {}, **self.extra)
        self.assertEqual(response.status_code, 200)

    def test_put(self):
        response = self.client.put('/api/language/Du/', {'name': 'dutch'}, **self.extra)
        self.assertEqual(response.status_code, 200)
        
    def test_delete(self):
        response = self.client.delete('/api/language/Du/', {}, **self.extra)
        self.assertEqual(response.status_code, 204)

    def test_post(self):               
        response = self.client.post('/api/language', { 'name':'Urdu' ,'code':'Ur','lname':'Urdu' ,'charset':'UTF-8'} , **self.extra)
        self.assertEqual(response.status_code, 200)



"""
class MyFuncTestCase(TestCase):
    def testBasic(self):
        a = ['larry', 'curly', 'moe']
        self.assertEquals(my_func(a, 0), 'larry')
        self.assertEquals(my_func(a, 1), 'curly')
        
"""
