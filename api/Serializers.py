from rest_framework import serializers
from student.models import Student

class StudentSerializer(serializers.ModelSerializerodelserializer):
    class meta:
        model = Student
        fields= "_ all _"

