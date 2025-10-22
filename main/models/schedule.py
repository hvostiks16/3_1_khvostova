from django.db import models
from .classroom import Classroom
from .teacher import Teacher
from .form import Form

class Schedule(models.Model):
    class AllowedDay(models.TextChoices):
        MONDAY = 'MONDAY', 'Monday'
        TUESDAY = 'TUESDAY', 'Tuesday'
        WEDNESDAY = 'WEDNESDAY', 'Wednesday'
        THURSDAY = 'THURSDAY', 'Thursday'
        FRIDAY = 'FRIDAY', 'Friday'
        SATURDAY = 'SATURDAY', 'Saturday'
        SUNDAY = 'SUNDAY', 'Sunday'

    day = models.CharField(
        db_column="Day",
        max_length=10,
        choices=AllowedDay.choices,
        default=AllowedDay.SUNDAY)
    date = models.DateField(db_column="Date")
    time = models.TimeField(db_column="Time")
    subject = models.CharField(db_column="Subject", max_length=100)

    id_classroom = models.ForeignKey(Classroom, db_column='classroom', on_delete=models.SET_NULL, null=True)
    id_teacher = models.ForeignKey(Teacher, db_column='teacher', on_delete=models.SET_NULL, null=True)
    id_form = models.ForeignKey(Form, db_column='form', on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'Schedule'
