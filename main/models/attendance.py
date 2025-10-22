from django.db import models
from .student import Student

class Attendance(models.Model):
    class AttendanceStatus(models.TextChoices):
        AVAILABLE = 'AVAILABLE', 'Available'
        UNAVAILABLE = 'UNAVAILABLE', 'Unavailable'

    date = models.DateField(db_column='Date', max_length=10)
    status = models.CharField(
        db_column='Status',
        max_length=11,
        choices=AttendanceStatus.choices,
        default=AttendanceStatus.UNAVAILABLE)
    amount_of_lessons = models.IntegerField(db_column='AmountOfLessons')


    id_student = models.ForeignKey(Student, db_column='idStudent', on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'Attendance'
