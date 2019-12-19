from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from .forms import TaskForm


# Create your views here.
def index(request):
    task = Task.objects.all()

    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid:
            form.save()
        return redirect('/')

    context = {
        "task" : task,
        "form" : form
    }
    return render(request, 'task/list.html', context)

def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    itemForm = TaskForm(instance=task)

    if request.method == 'POST':
        itemForm = TaskForm(request.POST, instance=task)
        if itemForm.is_valid:
            itemForm.save()
            return redirect('/')
    
    context = {
        'task' : task,
        'itemForm' : itemForm
    }
    return render(request, 'task/update_task.html', context)