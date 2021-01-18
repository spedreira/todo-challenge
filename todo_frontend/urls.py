from django.urls import path
from . import views

urlpatterns = [
    ####FRONT END URLS####
    path('', views.home, name='todo-home'),
    path('search/', views.search, name='todo-search'),
    path('about/', views.about, name='todo-about'),

]