from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
# Create your views here.

def home(self):
    task = Task.objects.filter(is_complete=False).order_by('-update_at')
    complete_task = Task.objects.filter(is_complete=True)

    context = {
        'task' : task,
        'complete_task': complete_task
    }
    return render(self, 'home.html')

def add_task(request):
    print(request.POST['task'])
    task=request.POST['task']
    Task.objects.create(task=task)

    return redirect('home')

def task_done(request, id):
    task=get_object_or_404(Task, id=id)
    task_is_complete=True
    task.save()

    return redirect('home')

def task_undone(request, id):
    task=get_object_or_404(Task, id=id)
    task_is_complete=False
    task.save()

    return redirect('home')

def edit_task(request, id):
    get_task=get_object_or_404(Task, id=id)
    if request.method == 'POST':
        new_task=request.POST['task']
        get_task.task=new_task
        get_task.save()
        return redirect('home')
    
    else:
        context = {
            'get_task' : get_task,
        }
        return render(request, 'edit_task.html', context)