from django.shortcuts import render, redirect
from .models import TaskModel
from django.utils.dateparse import parse_datetime
from django.utils.timezone import now
# Create your views here.
from django.contrib.auth.decorators import login_required

@login_required(login_url='login_')
def home(request):
  data = TaskModel.objects.filter(user = request.user, completed=False, trashed = False)
  return render(request,'home.html',{'data':data, 'now': now()})

@login_required
def add(request):
  if request.method =='POST':
    task = request.POST['task']
    desc = request.POST['desc']
    due_date_raw = request.POST.get('due_date')
    if due_date_raw:
      due_date = parse_datetime(due_date_raw)
    else:
      due_date = None

    TaskModel.objects.create(
      user = request.user,
      task = task,
      desc = desc,
      due_date = due_date
    )
    return redirect('home')
  return render(request,'add.html')


@login_required
def complete(request, id):
  task = TaskModel.objects.get(id = id)
  task.completed = True
  task.save()
  return redirect('home')


@login_required
def trash_task(request, id):
  task = TaskModel.objects.get(id = id)
  task.trashed = True
  task.save()
  return redirect('home')



def about(request):
  return render(request,'about.html')


@login_required
def complete_list(request):
  data = TaskModel.objects.filter(completed=True, trashed = False)
  return render(request, 'complete.html',{'data': data})


@login_required
def delete(request, id):
  TaskModel.objects.get(id = id).delete()
  return redirect('trash')

@login_required
def trash_list(request):
  data = TaskModel.objects.filter(trashed = True)
  return render(request, 'trash.html', {'data' : data})

def edit(request, id):
  task = TaskModel.objects.get(id = id)
  if request.method == 'POST':
    task.task = request.POST['task']
    task.desc = request.POST['desc']
    task.save()
    return redirect('home')
  return render(request, 'edit.html', {'task': task})

def restore(request, id):
  task = TaskModel.objects.get(id = id)
  task.trashed = False
  task.completed = False
  task.save()
  return redirect('trash')

