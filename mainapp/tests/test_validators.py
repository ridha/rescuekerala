from django.test import SimpleTestCase
from django.core.exceptions import ValidationError
from mainapp.validators import validate_phonenumber


class Test(SimpleTestCase):

    def test_invalid_phonenumber(self):
        with self.assertRaises(ValidationError):
            validate_phonenumber("12345678")

    def test_valid_phonenumber(self):
        validate_phonenumber("123 444 9999")
