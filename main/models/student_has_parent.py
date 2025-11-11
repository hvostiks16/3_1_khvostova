from django.db import models
from .parent import Parent
from .student import Student

class StudentHasParent(models.Model):
    parent = models.ForeignKey(Parent, on_delete=models.SET_NULL, null = True, db_column='idParent')
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null = True, db_column='idStudent')

    class Meta:
        db_table = 'Student_has_Parent'
