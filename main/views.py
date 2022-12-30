from django.shortcuts import render,redirect
from .models import Tasks
from .forms import TasksForm

#here we can control which template is going to be shown on cpecific site
def first(request):
    tasks = Tasks.objects.order_by("taskdeadline")
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def login(request):
    return render(request, 'main/login.html')


def tasks(request):
    tasks = Tasks.objects.order_by("taskdeadline")
    return render(request, 'main/tasks.html', {'page': 'Tasker','tasks': tasks })

def create_task(request):
    error = " "
    if request.method == 'POST':
        form = TasksForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home-page')
        else:
            error ="Data wasn`t valid"

    form =TasksForm()
    context={
        'form': form
    }
    return render(request, 'main/create_task.html',context)

