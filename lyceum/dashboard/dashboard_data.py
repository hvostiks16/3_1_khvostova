# dashboard_data.py
import pandas as pd
from main.repositories.analytics_repository import AnalyticsRepository
from main.repositories.statistics_repository import StatisticsRepository

def get_dashboard_data():
    data = {}

    data['students_count_by_form'] = pd.DataFrame(list(AnalyticsRepository.students_count_by_form()))
    data['books_per_form'] = pd.DataFrame(list(AnalyticsRepository.books_per_form()))
    data['parent_children_by_privilege'] = pd.DataFrame(list(AnalyticsRepository.parent_children_by_privilege()))
    data['risky_students_attendance'] = pd.DataFrame(list(AnalyticsRepository.risky_students_attendance()))
    data['privileged_students_per_form'] = pd.DataFrame(list(AnalyticsRepository.privileged_students_per_form()))
    data['books_per_student'] = pd.DataFrame(list(AnalyticsRepository.books_per_student()))
    data['risky_students_per_day'] = pd.DataFrame(list(AnalyticsRepository.risky_students_per_day()))

    return data

