from django.shortcuts import render,HttpResponse
from .models import Todo
from rest_framework import viewsets
from .serializers import todo_serializer
# Create your views here.

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = todo_serializer
