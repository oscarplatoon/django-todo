from django.shortcuts import render, redirect
from .forms import TodoForm
from .models import Todo

def get_todo(todo_id):
    return Todo.objects.get(id=todo_id)

def todo_list(request):
    todos_list = Todo.objects.all()
    todo_data = {'todos': todos_list}
    return render(request,'todo/todo_list.html', todo_data)

def todo_view(request, todo_id):
    todo = get_todo(todo_id)
    todo_data = {'todo':todo}
    return(render(request, 'todo/todo_detail.html', todo_data))

def todo_create(request):
    pass

def todo_update(request, todo_id):
    pass

def todo_delete(request, todo_id):
    pass