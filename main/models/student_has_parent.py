from django.db import models
from .parent import Parent
from .student import Student

class BookHasStudent(models.Model):
    id_parent = models.ForeignKey(Parent, on_delete=models.SET_NULL, null = True, db_column='idParent')
    id_student = models.ForeignKey(Student, on_delete=models.SET_NULL, null = True, db_column='idStudent')

    class Meta:
        db_table = 'Student_has_Parent'
