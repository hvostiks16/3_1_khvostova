import plotly.express as px
import pandas as pd

from .dashboard_data import get_dashboard_data

def dashboard_plotly_components(filters=None):
    data = get_dashboard_data()
    figs = {}

    # 1. Бар: студенти по класах
    df = data['students_count_by_form'].copy()
    if not df.empty and {'idClass', 'name', 'student_count'}.issubset(df.columns):
        df['student_count'] = pd.to_numeric(df['student_count'], errors='coerce').fillna(0)
        df = df.groupby(['idClass', 'name'], as_index=False)['student_count'].sum()
        fig = px.bar(df, x='name', y='student_count',
                     title='Кількість студентів по класах',
                     labels={'name': 'Клас', 'student_count': 'Студентів'})
    else:
        fig = px.bar(title="Немає даних")
    figs['students_by_form'] = fig.to_dict()

    # 2. Pie: книги по класах
    df = data['books_per_form'].copy()
    if not df.empty and {'name', 'books_count'}.issubset(df.columns):
        df['books_count'] = pd.to_numeric(df['books_count'], errors='coerce').fillna(0)
        df = df.groupby(['name'], as_index=False)['books_count'].sum()
        fig = px.pie(df, names='name', values='books_count', title='Кількість книг по класах')
    else:
        fig = px.pie(title="Немає даних")
    figs['books_per_form'] = fig.to_dict()

    # 3. Бар: ризикові студенти
    df = data['risky_students_attendance'].copy()
    if not df.empty and {'surname', 'missed_lessons'}.issubset(df.columns):
        df['missed_lessons'] = pd.to_numeric(df['missed_lessons'], errors='coerce').fillna(0)
        df = df.groupby(['surname'], as_index=False)['missed_lessons'].sum()
        fig = px.bar(df, x='surname', y='missed_lessons',
                     title='Пропущені уроки студентами',
                     labels={'surname': 'Студент', 'missed_lessons': 'Пропущено'})
    else:
        fig = px.bar(title="Немає даних")
    figs['risky_students'] = fig.to_dict()

    # 4. Бар: батьки з пільговими дітьми
    df = data['parent_children_by_privilege'].copy()
    if not df.empty and {'surname', 'privileged_children'}.issubset(df.columns):
        df['privileged_children'] = pd.to_numeric(df['privileged_children'], errors='coerce').fillna(0)
        df = df.groupby(['surname'], as_index=False)['privileged_children'].sum()
        fig = px.bar(df, x='surname', y='privileged_children',
                     title='Батьки з пільговими дітьми',
                     labels={'surname': 'Батько/Мати', 'privileged_children': 'К-сть дітей'})
    else:
        fig = px.bar(title="Немає даних")
    figs['privileged_children'] = fig.to_dict()

    # 5. Бар: привілейовані студенти по формах
    df = data['privileged_students_per_form'].copy()
    if not df.empty and {'name', 'privileged_students'}.issubset(df.columns):
        df['privileged_students'] = pd.to_numeric(df['privileged_students'], errors='coerce').fillna(0)
        df = df.groupby(['name'], as_index=False)['privileged_students'].sum()
        fig = px.bar(df, x='name', y='privileged_students',
                     title='Привілейовані студенти по формах',
                     labels={'name': 'Клас', 'privileged_students': 'Студентів'})
    else:
        fig = px.bar(title="Немає даних")
    figs['privileged_students'] = fig.to_dict()

    # 6. Бар: книги на студента
    df = data['books_per_student'].copy()
    if not df.empty and {'surname', 'books_count'}.issubset(df.columns):
        df['books_count'] = pd.to_numeric(df['books_count'], errors='coerce').fillna(0)
        df = df.groupby(['surname'], as_index=False)['books_count'].sum()
        fig = px.bar(df, x='surname', y='books_count',
                     title='Кількість книг на студента',
                     labels={'surname': 'Студент', 'books_count': 'Книг'})
    else:
        fig = px.bar(title="Немає даних")
    figs['books_per_student'] = fig.to_dict()

    # 7. Лінія: ризикові студенти по днях
    df = data['risky_students_per_day'].copy()
    if not df.empty and {'date', 'risky_count'}.issubset(df.columns):
        df['date'] = pd.to_datetime(df['date'], errors='coerce')
        df['risky_count'] = pd.to_numeric(df['risky_count'], errors='coerce').fillna(0)
        df = df.dropna(subset=['date']).groupby(['date'], as_index=False)['risky_count'].sum()
        fig = px.line(df, x='date', y='risky_count',
                      title='Кількість ризикових студентів по днях',
                      labels={'date': 'Дата', 'risky_count': 'Кількість'})
    else:
        fig = px.line(title="Немає даних")
    figs['risky_students_per_day_line'] = fig.to_dict()

    return figs
