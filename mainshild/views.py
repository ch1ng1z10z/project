from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import task
from .serializers import TaskSerializer

class TaskListCreateView(ListCreateAPIView):
    queryset = task.objects.all()
    serializer_class = TaskSerializer

class TaskDetailView(RetrieveUpdateDestroyAPIView):
    queryset = task.objects.all()
    serializer_class = TaskSerializer