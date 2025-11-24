from django import forms
from .models import Teacher, Student, Parent

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['name', 'surname', 'patronymic', 'phone_number', 'email']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'name', 'surname', 'patronymic', 'phone_number', 'email',
            'privilege', 'date_of_birth', 'city', 'neighborhood',
            'street', 'building', 'apartment', 'id_form', 'parents'
        ]

class ParentForm(forms.ModelForm):
    class Meta:
        model = Parent
        fields = ['name', 'surname', 'patronymic', 'phone_number', 'email']