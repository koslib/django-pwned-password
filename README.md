# django-pwned-password
Validate user passwords against haveibeenpwned.com database.

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

# Contributing
Feel free to send any PRs or open issues with ideas for implementation.