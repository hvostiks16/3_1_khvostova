from rest_framework import serializers
from .models import (
    Book, Classroom, Form, Parent, Schedule, Student, Teacher
)

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('idBook', 'name', 'author', 'date_of_publication', 'date_of_borrowing', 'status')
        read_only_fields = ('idBook',)

class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ('idClassroom', 'type', 'capacity', 'equipment')
        read_only_fields = ('idClassroom',)

class FormSerializer(serializers.ModelSerializer):
    id_teacher = serializers.PrimaryKeyRelatedField(queryset=Teacher.objects.all())
    id_parent = serializers.PrimaryKeyRelatedField(queryset=Parent.objects.all())

    class Meta:
        model = Form
        fields = ('idClass', 'name', 'id_teacher', 'id_parent')
        read_only_fields = ('idClass',)

class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = ('idParent', 'name', 'surname', 'patronymic', 'phone_number', 'email')
        read_only_fields = ('idParent',)

class ScheduleSerializer(serializers.ModelSerializer):
    id_teacher = serializers.PrimaryKeyRelatedField(queryset=Teacher.objects.all())
    id_classroom = serializers.PrimaryKeyRelatedField(queryset=Classroom.objects.all())
    id_form = serializers.PrimaryKeyRelatedField(queryset=Form.objects.all())

    class Meta:
        model = Schedule
        fields = ('day', 'date', 'time', 'subject', 'id_classroom', 'id_teacher', 'id_form')

class StudentSerializer(serializers.ModelSerializer):
    id_form = serializers.PrimaryKeyRelatedField(queryset=Form.objects.all())

    class Meta:
        model = Student
        fields = ('idStudent', 'name', 'surname', 'patronymic', 'phone_number', 'email', 'privilege', 'date_of_birth',
                  'city', 'neighborhood', 'street', 'building', 'apartment', 'id_form')
        read_only_fields = ('idStudent',)

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('idTeacher', 'name', 'surname', 'patronymic', 'phone_number', 'email')
        read_only_fields = ('idTeacher',)