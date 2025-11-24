from django.db import models
from .book import Book
from .student import Student

class BookHasStudent(models.Model):
    idBookHasStudent = models.AutoField(primary_key=True, db_column='idBookHasStudent')
    id_book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True, db_column='idBook')
    id_student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True, db_column='idStudent')

    class Meta:
        db_table = 'Book_has_Student'
