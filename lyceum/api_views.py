import pandas as pd
from rest_framework.views import APIView
from rest_framework.response import Response

from main.repositories.analytics_repository import AnalyticsRepository
from main.repositories.statistics_repository import StatisticsRepository

class FormsStudentsCountAPI(APIView):
    def get(self, request):
        qs = AnalyticsRepository.students_count_by_form()
        df = pd.DataFrame(list(qs))
        return Response(df.to_dict(orient='records'))

class BooksPerFormAPI(APIView):
    def get(self, request):
        qs = AnalyticsRepository.books_per_form()
        df = pd.DataFrame(list(qs))
        return Response(df.to_dict(orient='records'))

class ParentChildrenByPrivilegeAPI(APIView):
    def get(self, request):
        qs = AnalyticsRepository.parent_children_by_privilege()
        df = pd.DataFrame(list(qs))
        return Response(df.to_dict(orient='records'))

class RiskyStudentsAttendanceAPI(APIView):
    def get(self, request):
        qs = AnalyticsRepository.risky_students_attendance()
        df = pd.DataFrame(list(qs))
        return Response(df.to_dict(orient='records'))

class PrivilegedStudentsPerFormAPI(APIView):
    def get(self, request):
        qs = AnalyticsRepository.privileged_students_per_form()
        df = pd.DataFrame(list(qs))
        return Response(df.to_dict(orient='records'))


class BooksPerStudentAPI(APIView):
    def get(self, request):
        qs = AnalyticsRepository.books_per_student()
        df = pd.DataFrame(list(qs))
        return Response(df.to_dict(orient='records'))

class RiskyStudentsPerDayAPI(APIView):
    def get(self, request):
        qs = AnalyticsRepository.risky_students_per_day()
        df = pd.DataFrame(list(qs))

        if df.empty or not {'date', 'risky_count'}.issubset(df.columns):
            return Response([])

        df['date'] = pd.to_datetime(df['date'], errors='coerce')
        df['risky_count'] = pd.to_numeric(df['risky_count'], errors='coerce').fillna(0)
        df = df.dropna(subset=['date']).groupby(['date'], as_index=False)['risky_count'].sum()

        return Response(df.to_dict(orient='records'))

class StudentAgeStatsAPI(APIView):
    def get(self, request):
        stats = StatisticsRepository.student_age_stats()
        return Response(stats)


class ClassroomCapacityStatsAPI(APIView):
    def get(self, request):
        stats = StatisticsRepository.classroom_capacity_stats()
        return Response(stats)


class AverageAgePerFormAPI(APIView):
    def get(self, request):
        qs = StatisticsRepository.average_age_per_form()
        return Response(qs)


class AverageAgeByPrivilegeAPI(APIView):
    def get(self, request):
        qs = StatisticsRepository.average_age_by_privilege()
        return Response(qs)


class MaxBooksPerStudentPerFormAPI(APIView):
    def get(self, request):
        qs = StatisticsRepository.max_books_per_student_per_form()
        return Response(qs)
