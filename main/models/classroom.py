from django.db import models
from .teacher import Teacher

class Classroom(models.Model):
    class ClassroomStatus(models.TextChoices):
        LECTURE = 'LECTURE', 'Lecture'
        LAB = 'LAB', 'Lost'
        WORKSHOP = 'WORKSHOP', 'Workshop'
        COMPUTER = 'COMPUTER', 'Computer'
        LANGUAGE = 'LANGUAGE', 'Language'
        ART = 'ART', 'Art'
        MUSIC = 'MUSIC', 'Music'
        GYM = 'GYM', 'Gym'
        LIBRARY = 'LIBRARY', 'Library'
        MEETING = 'MEETING', 'Meeting'
        EXAM = 'EXAM', 'Exam'
        MULTIMEDIA = 'MULTIMEDIA', 'Multimedia'

    type = models.CharField(
        db_column='Status',
        max_length=10,
        choices=ClassroomStatus.choices,
        default=ClassroomStatus.LECTURE)
    capacity = models.PositiveIntegerField(db_column='Capacity')
    equipment = models.CharField(db_column='Equipment', max_length=45)

    id_teacher = models.ForeignKey(Teacher, db_column='Teacher', on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'Classroom'