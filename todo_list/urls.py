
from django.contrib import admin
from django.urls import path
from mainshild.urls import mainshildurlpatterns
from mainshild.views import TaskListCreateView, TaskDetailView


urlpatterns = mainshildurlpatterns + [
    path('admin/', admin.site.urls),
]
