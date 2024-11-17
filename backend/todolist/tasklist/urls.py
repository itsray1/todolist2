from django.urls import path
from . import views

urlpatterns = [
    # path('', views.TodoListListCreateView.as_view(), name='todolist-list-create'),
    # path('todolists/<int:pk>/', views.TodolistRetrieveUpdateDestroyView.as_view(), name='todolist-detail'),
     path('', views.todo_list_create_view, name='todolist-list-create'),
     path('todolists/<int:pk>/', views.todo_view, name='todolist-detail'),
    
    # path('tasks/',views. TaskListCreateView.as_view(), name='task-list-create'),
    # path('tasks/<int:pk>/',views. TaskRetrieveUpdateDestroyView.as_view(), name='task-detail'),
     path('tasks/',views. task_create_view, name='task-detail'),
     path('tasks/<int:pk>/',views. task_view, name='task-detail'),

 


]
