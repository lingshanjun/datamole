from common import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'rwr4di0x1v!#k_d%7%3$)8^fb7_(vagv(8movzw(n4(*$xn)ja'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'datamole',
        'USER': 'datamole',
        'PASSWORD': 'datamole',
    }
}
