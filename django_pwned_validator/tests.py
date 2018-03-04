import random
import string

from django.core.exceptions import ValidationError
from django.contrib.auth import password_validation
from django.test import TestCase


class PwnedPasswordValidatorTests(TestCase):
    def setUp(self):
        self.obvious_pass = 'password1234'
        self.complex_pass = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(25))

    def test_failing_password(self):
        with self.assertRaises(ValidationError):
            password_validation.validate_password(self.obvious_pass)

    def test_succeeding_password(self):
        self.assertEqual(
            password_validation.validate_password(self.complex_pass),
            None
        )


