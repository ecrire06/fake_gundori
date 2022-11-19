from django.shortcuts import render, redirect
from .forms import SoldierForm
from .models import Soldier


def index(request):
    soldiers = Soldier.objects.all().values()
    content = {
        'soldiers': soldiers,
    }
    return render(request, 'index.html', content)

def addsoldier(request):
    if request.method == "POST":
        form = SoldierForm(request.POST)
        if form.is_valid():
            soldier = form.save(commit=False)
            soldier.save()
            return redirect('index')
        else:
            return redirect('index')
    else: # request.method == "GET"
        form = SoldierForm()
        return render(request, 'new.html', {'form': form})

def delete(request, id):
    soldier = Soldier.objects.get(id=id)
    soldier.delete()
    return redirect('index')

def update(request, id):
    soldier = Soldier.objects.get(id=id)
    if request.method == "POST":
        form = SoldierForm(request.POST, instance=soldier)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = SoldierForm(instance=soldier)
    return render(request, 'update.html', {'form' : form})