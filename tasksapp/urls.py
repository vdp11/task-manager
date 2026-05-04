from django.urls import path
from . import views
from .models import Task

urlpatterns = [
    path('', views.tasksapp, name='tasksapp'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'), 
]

