from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Count
from .models import (
    Book, Classroom, Form, Parent, Schedule, Student, Teacher
)
from .serializer import (
    BookSerializer, ClassroomSerializer, FormSerializer, ParentSerializer,
    ScheduleSerializer, StudentSerializer, TeacherSerializer
)
from .unit_of_work import UnitOfWork

repo = UnitOfWork()

class BookViewSet(viewsets.ModelViewSet):
    repository = repo.books
    queryset = repository.get_all()
    serializer_class = BookSerializer

class ClassroomViewSet(viewsets.ModelViewSet):
    repository = repo.classrooms
    queryset = repository.get_all()
    serializer_class = ClassroomSerializer

class FormViewSet(viewsets.ModelViewSet):
    repository = repo.forms
    queryset = repository.get_all()
    serializer_class = FormSerializer

class ParentViewSet(viewsets.ModelViewSet):
    repository = repo.parents
    queryset = repository.get_all()
    serializer_class = ParentSerializer

class ScheduleViewSet(viewsets.ModelViewSet):
    repository = repo.schedules
    queryset = repository.get_all()
    serializer_class = ScheduleSerializer

class StudentViewSet(viewsets.ModelViewSet):
    repository = repo.students
    queryset = repository.get_all()
    serializer_class = StudentSerializer

class TeacherViewSet(viewsets.ModelViewSet):
    repository = repo.teachers
    queryset = repository.get_all()
    serializer_class = TeacherSerializer

class StudentsPerClassReportView(APIView):
    def get(self, request):
        data = Form.objects.annotate(
            student_count=Count('students')  # підрахунок учнів у класі
        ).values('idClass', 'name', 'student_count')
        return Response(list(data))

class AvailableBooksView(APIView):
    def get(self, request):
        books = Book.objects.filter(status=Book.BookStatus.AVAILABLE)
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)