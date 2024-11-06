from django.urls import path
from . import views

urlpatterns = [
    path('', views.TodoListListCreateView.as_view(), name='todolist-list-create'),
    path('todolists/<int:pk>/', views.TodolistRetrieveUpdateDestroyView.as_view(), name='todolist-detail'),
    # path('todolists/<int:pk>/update/',views. TodoListUpdateView.as_view(), name='todolist-update'),
    # path('todolists/<int:pk>/delete/',views. TodoListDeleteView.as_view(), name='todolist-delete'),
    
    path('tasks/',views. TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/',views. TaskRetrieveUpdateDestroyView.as_view(), name='task-detail'),
    # path('tasks/<int:pk>/update/',views. TaskUpdateView.as_view(), name='task-update'),
    # path('tasks/<int:pk>/delete/',views. TaskDeleteView.as_view(), name='task-delete'),
]
