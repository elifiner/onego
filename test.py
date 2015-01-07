from djangone import *
from django.shortcuts import render

@url(r'^momo/?$')
def momo(request):
    return render(request, 'index.html', {'name': 'Momo'})

@url(r'^(\w+)?$')
def index(request, name):
    return render(request, 'index.html', {'name': name})

if __name__=='__main__':
    run()
