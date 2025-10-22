from django.db import models
from .book import Book
from .student import Student

class BookHasStudent(models.Model):
    id_book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
    id_student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'Book_has_Student'
