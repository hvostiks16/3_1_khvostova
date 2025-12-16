from django.contrib import admin
from main.models import (
    Student, Teacher, Parent, Book, Classroom,
    Attendance, Schedule, Form, BookHasStudent, StudentHasParent
)

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Parent)
admin.site.register(Book)
admin.site.register(Classroom)
admin.site.register(Attendance)
admin.site.register(Schedule)
admin.site.register(Form)
admin.site.register(BookHasStudent)
admin.site.register(StudentHasParent)
