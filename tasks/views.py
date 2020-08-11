from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from .models import * 
from .forms import * # imports the form to set up view


# Create your views here.
def index(request):     #create task
    tasks = Task.objects.all() #grab everything in task


    form = TaskForm() 

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'tasks': tasks, 'form': form}
    return render(request, 'tasks/list.html',context)

def updateTask(request, primarykey):    #upate task
    task = Task.objects.get(id = primarykey)

    form = TaskForm(instance=task) #make instance of the same item into the form

    if request.method == "POST": 
        form = TaskForm(request.POST, instance =task) #need instance so it overwrites not create a new one
        if form.is_valid:
            form.save()
        return redirect ('/')
    context = {'form': form}
    return render(request, 'tasks/update_task.html', context)


def completeTask(request,primarykey):
    task= Task.objects.get(id=primarykey)
    if request.method == "POST":
        setattr(task, 'complete', True)
        task.save()
        return redirect('/')
    context={'task' : task}
    return render(request, 'tasks/complete_task.html', context)

def deleteTask(request, primarykey):
    item = Task.objects.get(id=primarykey)
    if request.method == "POST":
        item.delete()
        return redirect('/')

    context={'item' : item}


    return render(request, 'tasks/delete.html', context)

