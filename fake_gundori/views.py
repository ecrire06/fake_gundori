from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .forms import SoldierForm
from .models import Soldier

# CRUD with Django built-in class-based generic views

class SoldierListView(generic.ListView):
    context_object_name = 'soldier_list'
    template_name = 'soldier_list.html'
    paginate_by = 10

    def get_queryset(self):
        return Soldier.objects.all().order_by('enter_date')

class SoldierCreateView(generic.CreateView):
    form_class = SoldierForm
    template_name = 'soldier_form.html'
    success_url = reverse_lazy('soldier-list')

class SoldierDetailView(generic.DetailView):
    model = Soldier
    template_name = 'soldier_detail.html'

class SoldierUpdateView(generic.UpdateView):
    model = Soldier
    form_class = SoldierForm
    template_name = 'soldier_update.html'
    success_url = reverse_lazy('soldier-list')

class SoldierDeleteView(generic.DeleteView):
    model = Soldier
    template_name = 'soldier_delete.html'
    success_url = reverse_lazy('soldier-list')

def index(request):
    soldiers = Soldier.objects.all().order_by('enter_date')
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

def detail(request, id):
    soldier = Soldier.objects.get(id=id)
    content = {
        'soldier': soldier,
    }
    return render(request, 'detail.html', content)