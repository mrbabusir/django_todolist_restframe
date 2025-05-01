from rest_framework import serializers
from .models import Todolist
# from .models import Todolist

class TodolistSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=200)
    description = serializers.CharField()
    is_completed = serializers.BooleanField(default=False)

    def create(self, validated_data):
        return Todolist.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.is_completed = validated_data.get('is_completed', instance.is_completed)
        instance.save()
        return instance