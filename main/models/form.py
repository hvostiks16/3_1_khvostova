from django.db import models
from .teacher import Teacher
from .parent import Parent

class Form(models.Model):
    name = models.CharField(db_column='Name', max_length=45)

    id_teacher = models.ForeignKey(Teacher, db_column='idTeacher', on_delete=models.SET_NULL, null=True)
    id_parent = models.ForeignKey(Parent, db_column='idParent', on_delete=models.SET_NULL, null=True)
    idClass = models.AutoField(primary_key=True, db_column='idClass')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        db_table = 'Class'
