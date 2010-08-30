import unittest
from django.test import TestCase
from a2b_cust.customer.models import Language
from function_def import my_func


class LanguageTestCase(unittest.TestCase):
    #fixtures = ['language.json']
    def setUp(self):
        self.dutch = Language.objects.create(code="Du", name="Dutch", lname="Dutch", charset="UTF-8")
        self.urdu = Language.objects.create(code="Ur", name="Urdu", lname="Urdu", charset="UTF-8")
        self.thai = Language.objects.create(code="Ti", name="Thani", lname="Thai", charset="UTF-8")
    """
    def test_models(self):
        self.assertEqual(Language.objects.all().count(), 3)
        
        self.assertEquals(Language.code, "Du")
        language = Language.objects.get(code="Du")

        self.assertEquals(language.name, 'Dutch')
        self.language.name = 'dutch'

        self.assertNotEquals(language.name, 'Dutch')
        self.assertEquals(language.name, 'dutch')
    """



class MyFuncTestCase(unittest.TestCase):
    def testBasic(self):
        a = ['larry', 'curly', 'moe']
        self.assertEquals(my_func(a, 0), 'larry')
        self.assertEquals(my_func(a, 1), 'curly')
