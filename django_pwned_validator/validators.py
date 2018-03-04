import requests
import hashlib

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _

PWNED_ENDPOINT = 'https://api.pwnedpasswords.com/'
PWNED_PASSWORD_CHECK_PATH = 'range/'


class PwnedPasswordValidator(object):

    def _exists_as_pwned(self, password):
        hash = hashlib.sha1(password.encode("utf8")).hexdigest().upper()
        head, rest = hash[:5], hash[5:]
        url = PWNED_ENDPOINT + PWNED_PASSWORD_CHECK_PATH + head
        req = requests.get(url)
        if rest in req.content.decode('utf-8'):
            # password found in pwned db
            return True
        else:
            return False

    def validate(self, password, *args, **kwargs):
        if self._exists_as_pwned(password):
            raise ValidationError(
                _('Password found in the `haveibeenpwned.com` database. Set a '
                  'more secure password instead')
            )

    def get_help_text(self):
        return _("Restrict passwords found in `haveibeenpwned.com` to be used")
