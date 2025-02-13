from rest_framework import serializers
from .models import Todo

class todo_serializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'
