from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Task
from .forms import TaskForm
from django.shortcuts import redirect, get_object_or_404
from .models import Task

#task = form.save(commit=False)
#task.user = request.user
#task.save() 

def tasksapp(request):
    
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = TaskForm()
    tasks = Task.objects.all()
    template = loader.get_template('myfirst.html')
    return render(request,'myfirst.html',{"tasks": tasks, "form": form})


def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.delete()
    return redirect('tasksapp') 

def edit_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('tasksapp')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasksapp/edit_task.html', {'form': form})   
# Create your views here.
