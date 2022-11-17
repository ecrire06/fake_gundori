# https://docs.djangoproject.com/en/4.1/topics/http/shortcuts/
# render(request, template_name, context=None, content_type=None, status=None, using=None)

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Soldier


def index(request):
    soldiers = Soldier.objects.all().values()
    content = {
        'soldiers': soldiers,
    }
    return render(request, 'index.html', content)

def add(request):
    return render(request, 'add.html')

def addrecord(request):
    name = request.POST['name']
    enter_date = request.POST['enter_date']
    army_choice = request.POST['army_choice']
    soldier = Soldier(name=name, enter_date=enter_date, army_choice=army_choice)
    soldier.save()
    return HttpResponseRedirect(reverse('index'))