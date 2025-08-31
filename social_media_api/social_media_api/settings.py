INSTALLED_APPS = [
    ...
    'rest_framework',
    'rest_framework.authtoken',  # For token authentication
    'accounts',
]
AUTH_USER_MODEL = 'accounts.CustomUser'

