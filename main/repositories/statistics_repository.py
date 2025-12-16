from django.db.models import Avg, Min, Max, Count
from django.db.models.functions import ExtractYear
from datetime import date
import pandas as pd
from lyceum.models import Student, Classroom, Form, Book

class StatisticsRepository:

    @staticmethod
    def student_age_stats():
        today_year = date.today().year
        qs = Student.objects.annotate(age=today_year - ExtractYear('date_of_birth')).values('age')
        df = pd.DataFrame(list(qs))
        if df.empty:
            return {}
        return {
            'average_age': df['age'].mean(),
            'median_age': df['age'].median(),
            'min_age': df['age'].min(),
            'max_age': df['age'].max()
        }

    @staticmethod
    def classroom_capacity_stats():
        qs = Classroom.objects.aggregate(
            min_capacity=Min('capacity'),
            max_capacity=Max('capacity'),
            average_capacity=Avg('capacity')
        )
        return qs

    @staticmethod
    def average_age_per_form():
        today_year = date.today().year
        qs = Student.objects.annotate(
            age=today_year - ExtractYear('date_of_birth')
        ).values('id_form__name').annotate(
            average_age=Avg('age'),
            students_count=Count('idStudent')
        ).order_by('-average_age')
        df = pd.DataFrame(list(qs))
        return df.to_dict(orient='records')

    @staticmethod
    def average_age_by_privilege():
        today_year = date.today().year
        qs = Student.objects.annotate(
            age=today_year - ExtractYear('date_of_birth')
        ).values('privilege').annotate(
            average_age=Avg('age'),
            students_count=Count('idStudent')
        ).filter(students_count__gt=0).order_by('-average_age')
        df = pd.DataFrame(list(qs))
        return df.to_dict(orient='records')

    @staticmethod
    def max_books_per_student_per_form():
        qs = Student.objects.values('id_form__name').annotate(
            books_count=Count('books')   # рахуємо кількість книг у студента
        ).values('id_form__name', 'books_count').order_by('-books_count')

        df = pd.DataFrame(list(qs))
        return df.to_dict(orient='records')