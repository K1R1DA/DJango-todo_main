from django.urls import path
from .views import home, add_task, task_done, task_undone, edit_task
urlpatterns = [
    path('', home, name='home'),
    path('add_task', add_task, name='add_task'),
    path('task_done/<int:id>/', task_done, name='task_done'),
    path('task_undone/<int:id>/', task_undone, name='task_undone'),
    path('edit_task/<int:id>/', edit_task, name='edit_task'),
]