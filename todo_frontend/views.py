from django.shortcuts import render

# Create your views here.

#FRONT VIEWS#
def home(request):
#    context = {
#        'tasks': Task.objects.all()
#    }
    return render(request, 'todo_frontend/home.html')


def search(request):
    return render(request, 'todo_frontend/search.html')


def about(request):
    context = {
        'title': 'Sobre esta App'
    }
    return render(request, 'todo_frontend/about.html', context)

