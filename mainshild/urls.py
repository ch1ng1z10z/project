
from django.urls import path

from mainshild.views import TaskListCreateView, TaskDetailView

mainshildurlpatterns = [
    path('tasks/', TaskListCreateView.as_view()),
    path('tasks/<int:pk>', TaskDetailView.as_view())
]
