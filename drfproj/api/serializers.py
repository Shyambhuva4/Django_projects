
from .models import Student
from rest_framework import serializers

class StudentSerializer(serializers.Serializer):
    
    name=serializers.CharField(max_length=100)
    city=serializers.CharField(max_length=100)

    def create(self,validate_data):
        return Student.objects.create(**validate_data)
