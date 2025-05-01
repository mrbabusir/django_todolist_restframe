from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Todolist
from .serializers import TodolistSerializer
from django.shortcuts import get_object_or_404
from rest_framework import status

# Create your views here.
@api_view(['GET', 'POST'])
def todolist_list(request):
    if request.method == 'GET':
        todolist = Todolist.objects.all()        
        serializer = TodolistSerializer(todolist, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TodolistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=status.HTTP_201_CREATED)
@api_view(['GET', 'PUT', 'DELETE','PATCH'])
def todolist_detail(request, id):
    if request.method == 'GET':
        todolist = get_object_or_404(Todolist, id=id)
        serializer = TodolistSerializer(todolist)
        return Response(serializer.data)
    elif request.method == 'PATCH':
        todolist = get_object_or_404(Todolist, id=id)
        serializer = TodolistSerializer(todolist, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT':
        todolist = get_object_or_404(Todolist, id=id)
        serializer = TodolistSerializer(todolist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        todolist = get_object_or_404(Todolist, id=id)
        todolist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
   

