from django.shortcuts import render
from .models import Task

from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer

#filtering data
from rest_framework import filters, generics


# Create your views here.

########## API VIEWS ###########

#info primary screen
@api_view(['GET'])
def apiUrlInfo(request):
    api_urls = {
		'Tareas':'/api/list/',
        'Crear':'/api/new/',
		'Detalles':'/api/detail/<str:pk>/',
		'Actualizar':'/api/update/<str:pk>/',
		'Eliminar':'/api/delete/<str:pk>/',
        'Filtrar': 'api/list/filter/?search=<str>'
		}
    return Response(api_urls)


@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all().order_by('-date_posted')
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def taskDetail(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(task, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def taskNew(request):
    serializer = TaskSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def taskUpdate(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def taskDelete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()

    return Response('Tarea eliminada')

#filtering#
class taskListFilter(generics.ListAPIView):
    queryset = Task.objects.all().order_by('-date_posted')
    serializer_class = TaskSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'date_posted']