from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from todos.models import Todo
from django.forms import ModelForm


class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'desc']


def get_todo(id):
    return Todo.objects.get(id=id)


# Views
def show_todos(request):
    todos = Todo.objects.all()
    context = {'todos': todos}
    return render(request, 'todos/show_todos.html', context)


def show_todo(request, id):
    todo = get_todo(id)
    context = {'todo': todo}
    return render(request, 'todos/show_todo.html', context)


def create_todo(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TodoForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            new_todo = form.save()
            return redirect('todos:show_todo', id=new_todo.id)
    # if a GET (or any other method) we'll create a blank form
    else:
        form = TodoForm()

    return render(request, 'todos/todo_form.html', {'form': form, 'type': "New"})


def edit_todo(request, id):
    todo = get_todo(id)

    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)

        if form.is_valid():
            updated_todo = form.save()
            return redirect('todos:show_todo', id=updated_todo.id)

    else:
        form = TodoForm(instance=todo)

    return render(request, 'todos/todo_form.html', {'form': form, 'type': 'Edit'})


def delete_todo(request, id):
    todo = get_todo(id)
    todo.delete()
    return redirect('todos:show_todos')
