from rest_framework import serializers
from models import task

class TaskSerializers(serializers.ModelSerializers):
    class Meta:
        model = task
        field = "__all__"