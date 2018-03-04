import requests

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _

PWNED_ENDPOINT = 'https://api.pwnedpasswords.com/'
PWNED_PASSWORD_CHECK_PATH = 'pwnedpassword/'


class PwnedPasswordValidator(object):

    def _exists_as_pwned(self, password):
        url = PWNED_ENDPOINT + PWNED_PASSWORD_CHECK_PATH + password
        req = requests.get(url)
        if req.status_code == 200:
            # password found in pwned db
            return True
        elif req.status_code >= 400:
            return False

    def validate(self, password, *args, **kwargs):
        if self._exists_as_pwned(password):
            raise ValidationError(
                _('Password found in the `haveibeenpwned.com` database. Set a '
                  'more secure password instead')
            )

    def get_help_text(self):
        return _("Restrict passwords found in `haveibeenpwned.com` to be used")
