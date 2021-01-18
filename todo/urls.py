from django.urls import path
from . import views

urlpatterns = [
    #### API URLS ####
    path('/', views.apiUrlInfo, name='todo-api'),
    path('/list/', views.taskList, name='todo-api-list'),
    path('/list/filter/', views.taskListFilter.as_view(), name='todo-api-list-filter'),
    path('/new/', views.taskNew, name='todo-api-new'),
    path('/detail/<str:pk>/', views.taskDetail, name='todo-api-detail'),
    path('/update/<str:pk>/', views.taskUpdate, name='todo-api-update'),
    path('/delete/<str:pk>/', views.taskDelete, name='todo-api-delete'),
]
