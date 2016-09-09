# -*- coding:utf-8 -*-

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

# datamole app abspath
DAPP_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# datamole project abpath
PROJECT_DIR = os.path.dirname(DAPP_DIR)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# Application definition

INSTALLED_APPS = (
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
    'member',
    'science',
    'news',
    'monograph',
    'pagination',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',

    'pagination.middleware.PaginationMiddleware',
)

ROOT_URLCONF = 'datamole.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(DAPP_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.core.context_processors.request',   # suit need
            ],
        },
    },
]

WSGI_APPLICATION = 'datamole.wsgi.application'

TEMPLATE_CONTEXT_PROCESSORS = (
                                "django.core.context_processors.auth",
                                "django.core.context_processors.debug",
                                "django.core.context_processors.i18n",
                                "django.core.context_processors.media",
                                "django.core.context_processors.request",
)


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'zh-CN'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
# upload path
MEDIA_ROOT = os.path.join(PROJECT_DIR, 'media')


# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(DAPP_DIR, 'statics'),
)

# suit config
# SUIT_CONFIG = {
#     'ADMIN_NAME':'后台管理系统',

#     'HEADER_DATE_FORMAT':'Y年m月d日 l',
#     'HEADER_TIME_FORMAT':'H:i',

#     # 'MENU':(
#     #     'sites',
#     #     {'app':'auth','lable':'认证'},
#     #     {'app':'dm','lable':'网站'},
#     # )
# }
