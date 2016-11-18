from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader

# Create your views here.
def index(request):
    template = loader.get_template('users/index.html')
    return HttpResponse(template.render(None, None))

def fullcalendar(request):
    template = loader.get_template('users/fullcalendar.html')
    return HttpResponse(template.render(None, None))
