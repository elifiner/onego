import djangone
from django.conf.urls import patterns
from django.shortcuts import render

def index(request, name):
    return render(request, 'index.html', {'name': name})

djangone.urlpatterns += patterns('', (r'^(?P<name>\w+)?$', index))

if __name__=='__main__':
    # run manage.py
    from django.core import management
    management.execute_from_command_line()