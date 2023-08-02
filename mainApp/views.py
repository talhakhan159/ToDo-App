from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *
# Create your views here.

class ListToDo(generics.ListAPIView):  #read
    queryset =ToDo.objects.all()
    serializer_class = ToDoSerializer
    
class DetailTodo(generics.RetrieveUpdateAPIView):   #update
    queryset =ToDo.objects.all()
    serializer_class = ToDoSerializer
    
class CreateToDo(generics.CreateAPIView):          #create
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    
class DeleteToDo(generics.DestroyAPIView):   #Delete
    queryset =ToDo.objects.all()
    serializer_class = ToDoSerializer       
    
    
    