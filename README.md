# django-pwned-password
Validate user passwords against haveibeenpwned.com database.

# Disclaimer
Think twice before using this package. Let your clients know you're testing their passwords against a 3rd-party service. Client trust
should be your #1 priority.
This projects only intends to highlight the need to ensure users select secure passwords, it is still a prototype and has not been tested in any production environment.  

# Scope
Restrict your Django project users from using a password that has been located even once in the haveibeenpwned.com database.
Doing this makes your project a more secure place for your clients.  

# Usage instructions
This package requires `requests` Python library. You can install it with
`pip install requests`, if it doesn't already exist in your project requirements.

1. Clone the repo inside your project
2. In your app's settings file, locate the `AUTH_PASSWORD_VALIDATORS` and
append the `PwnedPasswordValidator` validator.

```python
{
    'NAME': 'django_pwned_validator.validators.PwnedPasswordValidator',
}
```

You can check out the `example` project to get an idea of how it works.

# Credits
1. Reddit user `Poromenos` (https://www.reddit.com/r/django/comments/81z84w/validate_user_passwords_against_haveibeenpwnedcom/)


# Contributing
Feel free to send any PRs or open issues with ideas for implementation.