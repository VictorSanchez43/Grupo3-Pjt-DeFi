from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'franezal$default',
        'USER': 'franezal',
        'PASSWORD': 'P@55w0rD',
        'HOST': 'franezal.mysql.pythonanywhere-services.com',
        'PORT': '3306',
    }
}