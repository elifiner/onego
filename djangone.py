import os
import sys
from django.conf.urls import patterns

__all__ = ['settings', 'urlpatterns']

def fake_module(name):
    # creates a fake module in memory
    module = type(sys)(name)
    sys.modules[name] = module
    return module

urlconf = fake_module('urls')
urlpatterns = patterns('')
urlconf.urlpatterns = urlpatterns

# Django required settings
settings = fake_module('settings')
settings.DEBUG = True
settings.TEMPLATE_DEBUG = True
settings.ROOT_URLCONF = 'urls'
settings.DATABASES = { 'default': {} }
settings.TEMPLATE_DIRS = ['.']
settings.SECRET_KEY = 'secret'
settings.MIDDLEWARE_CLASSES = {}

# let Django know about the fake settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
