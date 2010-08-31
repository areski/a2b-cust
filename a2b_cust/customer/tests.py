import urllib, base64
from django.contrib.auth.models import User
from django.test import TestCase
from a2b_cust.customer.models import *
from function_def import my_func


class LanguageTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('admin', 'admin@world.com', 'admin')
        self.user.is_staff = True
        self.user.is_superuser = True
        self.user.is_active = True
        self.user.save()
        self.auth_string = 'Basic %s' % base64.encodestring('admin:admin').rstrip()

        self.dutch = Language.objects.create(code="Du", name="Dutch", lname="Dutch", charset="UTF-8")

    def test_get(self):
        response = self.client.get('/api/language/')
        self.assertEquals(response.status_code, 401)

        auth_string = 'Basic %s' % base64.encodestring('%s:%s' % ('admin', 'admin')).rstrip()
        response = self.client.get('/api/language/', HTTP_AUTHORIZATION=auth_string)
        self.assertEquals(response.status_code, 200, 'Failed with combo of %s:%s' % ('admin', 'admin'))
    
    """
    def test_post(self):
        r = self.client.post('/api/language/', {'code': 'Ur', 'name': 'Urdu' ,'lname': 'Urdu' ,'charset': 'UTF-8', },content_type="text/xml")
        try :
            self.assertEqual(r.status_code, 200)
        except :
            self.assertEqual(r.status_code, 401)

    def test_put(self):
        r = self.client.put('/api/language/Ur/', {'name': 'Urdu'})
        self.assertEqual(r.status_code, 200)

    def test_delete(self):
        r = self.client.delete('/api/language/Ur/', {})
        self.assertEqual(r.status_code, 200)
    """


"""
class MyFuncTestCase(TestCase):
    def testBasic(self):
        a = ['larry', 'curly', 'moe']
        self.assertEquals(my_func(a, 0), 'larry')
        self.assertEquals(my_func(a, 1), 'curly')
        
"""
