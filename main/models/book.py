from django.db import models

class Book(models.Model):
    class BookStatus(models.TextChoices):
        AVAILABLE = 'AVAILABLE', 'Available'
        BORROWED = 'BORROWED', 'Borrowed'
        LOST = 'LOST', 'Lost'
        DAMAGED = 'DAMAGED', 'Damaged'
        RESERVED = 'RESERVED', 'Reserved'

    name = models.CharField(db_column='Name', max_length=50)
    author = models.CharField(db_column='Author', max_length=50)
    date_of_publication = models.DateField(db_column='DateOfPublication', max_length=10)
    date_of_borrowing = models.DateField(db_column='DateOfBorrowing', max_length=10)
    status = models.CharField(
        db_column='Status',
        max_length=10,
        choices=BookStatus.choices,
        default=BookStatus.AVAILABLE)
    idBook = models.AutoField(primary_key=True, db_column='idBook')

    class Meta:
        db_table = 'Book'