from django.shortcuts import render
from django.http import HttpResponse

from .models import *


# Create your views here.
def index(request):
    task = Task.objects.all()

    context = {
        "task" : task
    }
    return render(request, 'task/list.html', context)