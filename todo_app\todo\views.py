from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm

def index(request):
    todos = Todo.objects.all()
    return render(request, 'index.html', {'todos': todos})

def create_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TodoForm()
    return render(request, 'create_todo.html', {'form': form})

def update_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'update_todo.html', {'form': form, 'todo_id': todo_id})

def delete_todo(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    return redirect('index')