from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
# Create your views here.
def home(request):
    tasks = Task.objects.filter(is_completed=False).order_by('-update_at')
    completed_tasks = Task.objects.filter(is_completed=True)

    context = {
        'tasks': tasks,
        'completed_tasks': completed_tasks
    }
    return render(request, 'home.html', context)

def add_task(request):
    print(request.POST['task'])
    task = request.POST['task']
    Task.objects.create(task=task)

    return redirect('home')

def task_done(request, id):
    task = get_object_or_404(Task, id=id)
    task.is_completed = True
    task.save()

    return redirect('home')

def task_undone(request, id):
    task = get_object_or_404(Task, id=id)
    task.is_completed = False
    task.save()

    return redirect('home')

def edit_task(request, id):
    get_task = get_object_or_404(Task, id=id)
    if request.method == 'POST':
        new_task = request.POST['task']
        get_task.task = new_task
        get_task.save()
        return redirect('home')
    else:
        context = {
            'get_task': get_task,
        }
        return render(request, 'edit_task.html', context)