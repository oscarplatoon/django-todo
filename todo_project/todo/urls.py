from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('<int:todo_id>', views.todo_view, name='todo_view'),
    path('new', views.todo_create, name='todo_new'),
    path('edit/<int:todo_id>', views.todo_update, name='todo_edit'),
    path('delete/<int:todo_id>', views.todo_delete, name='todo_delete'),
]

