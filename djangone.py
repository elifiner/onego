import os
import sys

import django
from django.conf.urls import patterns
from django.core import management

__all__ = ['settings', 'url', 'manage', 'run']

def fake_module(name):
    # creates a fake module in memory
    module = type(sys)(name)
    sys.modules[name] = module
    return module

def url(regex, params=None):
    # a decorator to bind a view to a url
    def _route(view):
        urlconf.urlpatterns += patterns('', (regex, view, params))
        def wrapper(*args, **kw):
            return view(*args, **kw)
        return wrapper
    return _route

def manage():
    management.execute_from_command_line()

def run():
    django.setup()
    management.call_command('runserver')

# Set up urlconf
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
