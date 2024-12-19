from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('todo_create/', views.todo_create, name='todo_create'),
    path('<int:todo_id>/todo_delete/', views.todo_delete, name='todo_delete'),
]