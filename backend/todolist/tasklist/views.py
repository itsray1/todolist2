from django.shortcuts import render
# Create your views here.
from rest_framework import generics, permissions,authentication
from .models import TodoList, Task
from .serializers import TodoListSerializer, TaskSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import api_view, permission_classes,authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def todo_list_create_view(request):
    if request.method == 'GET':
        todos = TodoList.objects.filter(creator=request.user)  
        serializer = TodoListSerializer(todos, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = TodoListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(creator=request.user) 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def todo_view(request, pk):
        try:
        
            todo = TodoList.objects.get(pk=pk, creator=request.user)
        except TodoList.DoesNotExist:
            return Response({"error": "Todo not found or not authorized"}, status=status.HTTP_404_NOT_FOUND)


        if request.method == 'GET':
            serializer = TodoListSerializer(todo)
            return Response(serializer.data)


        elif request.method == 'PUT':
            serializer = TodoListSerializer(todo, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        
        elif request.method == 'DELETE':
            todo.delete()
            return Response({"message": "Todo deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

# class TodoListListCreateView(generics.ListCreateAPIView):
    # queryset = TodoList.objects.all()
    # serializer_class = TodoListSerializer
    # authentication_classes = [JWTAuthentication] 
    # permission_classes = [permissions.IsAuthenticated]

    # def perform_create(self, serializer):
    #     serializer.save(creator=self.request.user)

    
    # def get_queryset(self):
    #  creator = self.request.user
    #  if not creator.is_authenticated:
    #         return TodoList.objects.none()
    #  return TodoList.objects.filter(creator=creator)


# class TodolistRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    # queryset = TodoList.objects.all()
    # serializer_class = TodoListSerializer
    # authentication_classes = [JWTAuthentication] 
    # permission_classes = [permissions.IsAuthenticated]
      
    # def get_queryset(self):
    #   return TodoList.objects.filter(creator=self.request.user)



###############################################################

@api_view(['GET', 'POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def task_create_view(request):
    if request.method == 'GET':
        tasks = Task.objects.filter(todolist__creator=request.user)
        if tasks.exists():
            serializer = TaskSerializer(tasks, many=True)
            return Response(serializer.data)
        else:
            return Response({"message": "No tasks found"}, status=200)
            
    
    elif request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def task_view(request, pk):
        try:
            tasks = Task.objects.get(pk=pk, todolist__creator=request.user)
        except Task.DoesNotExist:
            return Response({"error": "Task not found or not authorized"}, status=status.HTTP_404_NOT_FOUND)


        if request.method == 'GET':
            serializer = TaskSerializer(tasks)
            return Response(serializer.data)


        elif request.method == 'PUT':
            serializer = TaskSerializer(tasks, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        
        elif request.method == 'DELETE':
            tasks.delete()
            return Response({"message": "Task deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

#  class TaskListCreateView(generics.ListCreateAPIView):
    # queryset = Task.objects.all()
    # serializer_class = TaskSerializer
    # authentication_classes = [JWTAuthentication] 
    # permission_classes = [permissions.IsAuthenticated]

    # def perform_create(self, serializer):
    #     serializer.save()
    
    # def get_queryset(self):
    #     user = self.request.user
    #     if not user.is_authenticated:
    #         return Task.objects.none()
    #     return Task.objects.filter(todolist__creator=user)
    
    # def get_serializer_context(self):
    #     return {'request': self.request}
   

# class TaskRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    # queryset = TodoList.objects.all()
    # serializer_class = TaskSerializer
    # authentication_classes = [JWTAuthentication] 
    # # permission_classes = [permissions.IsAuthenticated]
      
    # def get_queryset(self):
    #   return Task.objects.filter(todolist__creator=self.request.user)



############################################################
   # def get_queryset(self,*args,**kwargs):
    #     qs=super().get_queryset(*args,**kwargs) 
    #     request=self.request
    #     user=request.user
    #     if not user.is_authenticated:
    #         return Task.objects.none()
    #     return qs.filter(creater=request.user)   
    #     
    # def get_queryset(self, request):
    #     qs = super().get_queryset(request)
    #     if request.user.is_superuser:
    #         return qs
    #     return qs.filter(todolist__creator=request.user)