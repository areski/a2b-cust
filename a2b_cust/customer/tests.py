import unittest
from django.test import TestCase, Client
from a2b_cust.customer.models import Language
from function_def import my_func


class LanguageTestCase(TestCase):
    #fixtures = ['language.json']
    
    def setUp(self):
        self.client = Client()
        self.dutch = Language.objects.create(code="Du", name="Dutch", lname="Dutch", charset="UTF-8")    

    def test_get(self):
        r = self.client.get('/api/language/Du/')
        self.failUnlessEqual(r.status_code, 200)

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



class MyFuncTestCase(unittest.TestCase):
    def testBasic(self):
        a = ['larry', 'curly', 'moe']
        self.assertEquals(my_func(a, 0), 'larry')
        self.assertEquals(my_func(a, 1), 'curly')
