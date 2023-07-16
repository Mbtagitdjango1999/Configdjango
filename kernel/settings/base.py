
import os
from pathlib import Path

from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent



DEFAULT_APPS =[
    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'kernel.urls'


TEMPLATES_DIR =os.path.join(BASE_DIR,config('TEMPLATE_DIR'))

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR,os.path.join(BASE_DIR,config('TEMPLATE_DIR'))],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'kernel.wsgi.application'





STATIC_URL = config('STATIC_URL')


STATICFILES_DIRS = (
    os.path.join(BASE_DIR , config('STATIC_DIR')),
    )

STATIC_ROOT =os.path.join(BASE_DIR , config('COLLECT_STATIC_DIR'))

MEDIA_URL = config('MEDIA_URL')

MEDIA_ROOT = config('MEDIA_UPLOAD_DIR')


DEFAULT_AUTO_FIELD= 'django.db.models.AutoField'




# FIXTURS_DIRS= tuple(
#     config('FIXTURE_TEST_DIRS',cast=tuple)
# )