import unittest
from django.test import TestCase
from a2b_cust.customer.models import Language


class LanguageTestCase(unittest.TestCase):
    #fixtures = ['language.json']
    def setUp(self):
        self.dutch = Language.objects.create(code="Du", name="Dutch", lname="Dutch", charset="UTF-8")
        self.urdu = Language.objects.create(code="Ur", name="Urdu", lname="Urdu", charset="UTF-8")
        self.thai = Language.objects.create(code="Ti", name="Thani", lname="Thai", charset="UTF-8")
    """
    def test_models(self):
        self.assertEqual(self.Language.all().count(), 3)
        self.assertEquals(self.Language.code, "Du")
        language = Language.objects.get(code="Du")

        self.assertEquals(language.name, 'Dutch')
        self.language.name = 'dutch'

        self.assertNotEquals(self.language.name, 'Dutch')
        self.assertEquals(self.language.name, 'dutch')
     """


