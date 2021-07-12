from django.shortcuts import render, redirect
from django.forms import ModelForm

from todo_app.models import Todo

class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description']

def get_todo(todo_id):
  return Todo.objects.get(id=todo_id)

def todo_list(request):
    todos = Todo.objects.all()
    data = {'all_todos': todos}
    return render(request, 'todo_app/todo_list.html', data)

def todo_view(request, todo_id):
    todo= get_todo(todo_id)
    data = {'todo': todo}
    return render(request, 'todo_app/todo_view.html', data)

def todo_create(request):
    form = TodoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('todos:todo_list')
    return render(request, 'todo_app/todo_edit.html', {'form': form, 'new_or_edit': 'New'})

def todo_update(request, todo_id):
    todo= get_todo(todo_id)
    form = TodoForm(request.POST or None, instance=todo)
    if form.is_valid():
        form.save()
        return redirect('todos:todo_list')
    return render(request, 'todo_app/todo_edit.html', {'form' :form, 'new_or_edit': 'Edit'})

def todo_delete(request, todo_id):
    todo= get_todo(todo_id)
    if request.method=='POST':
        todo.delete()
        return redirect('todos:todo_list')
    return render(request, 'todo_app/todo_delete.html', {'object':todo})