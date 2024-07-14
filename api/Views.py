
from rest_framework.response import responses
from rest_framework.views import APIview
from student.modules import Student
from serializers import  StudentSerializer

class StudentListView(APIView):
    def get(self,request):
        student = Student.object.all()
        serializer = StudentSerializer(students,many=True)
        return Response(serializer.data)
        

