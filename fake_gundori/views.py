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
    if request.method == "GET":
        form = SoldierForm()
        return render(request, 'new.html', {'form': form})