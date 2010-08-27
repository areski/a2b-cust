import unittest
from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import simplejson
from django.conf import settings

from a2b_cust.customer.models import Language


class LanguageTestCase(unittest.TestCase):
    fixtures = ['language.json']
    def setUp(self):
        self.dutch = Language.objects.create(code="Du", name="Dutch", lname="Dutch", charset="UTF-8")
        self.urdu = Language.objects.create(code="Ur", name="Urdu", lname="Urdu", charset="UTF-8")
        self.thai = Language.objects.create(code="Ti", name="Thani", lname="Thai", charset="UTF-8")

    def test_edit(self):
        language = Language.objects.get(code='Du')
        language.lname = "dutch"
        language.save()




