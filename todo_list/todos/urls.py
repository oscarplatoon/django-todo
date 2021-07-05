from django.urls import include, path
from todos import views

app_name = 'todos'

urlpatterns = [
    path('', views.show_todos, name='show_todos'),
    path('<int:id>/', views.show_todo, name='show_todo'),
    path('new/', views.create_todo, name='create_todo'),
    path('<int:id>/edit/', views.edit_todo, name='edit_todo'),
    path('<int:id>/delete/', views.delete_todo, name='delete_todo'),
]
