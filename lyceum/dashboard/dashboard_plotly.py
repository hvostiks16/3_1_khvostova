import pandas as pd
import plotly.graph_objects as go
from .dashboard_data import get_dashboard_data

def dashboard_plotly_components(filters=None):
    data = get_dashboard_data()
    figs = {}

    def bar_chart(x, y, title, x_label, y_label, color="#1f77b4"):
        x = [str(val) for val in x]
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=x,
            y=y,
            marker_color=color,
            hoverinfo='x+y'
        ))
        fig.update_layout(
            title=title,
            xaxis_title=x_label,
            yaxis_title=y_label,
            xaxis=dict(
                type='category',
                tickmode='array',
                tickvals=x,
                ticktext=x,
                tickangle=-45
            ),
            margin=dict(t=50, b=100),
            height=400
        )
        return fig.to_dict()

    def pie_chart(labels, values, title):
        labels = [str(val) for val in labels]
        fig = go.Figure()
        fig.add_trace(go.Pie(
            labels=labels,
            values=values,
            hoverinfo='label+value+percent',
            textinfo='label+percent'
        ))
        fig.update_layout(
            title=title,
            height=400,
            legend=dict(
                title="Категорії",
                itemsizing='constant'
            )
        )
        return fig.to_dict()

    def line_chart(x, y, title, x_label, y_label):
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=x, y=y, mode='lines+markers', line=dict(width=2)))
        fig.update_layout(
            title=title,
            xaxis_title=x_label,
            yaxis_title=y_label,
            xaxis=dict(type='date'),
            margin=dict(t=50, b=50),
            height=400
        )
        return fig.to_dict()


    # 1. Студенти по класах
    df = data['students_count_by_form'].copy()
    if not df.empty and {'name', 'student_count'}.issubset(df.columns):
        df['name'] = df['name'].astype(str)
        df['student_count'] = pd.to_numeric(df['student_count'], errors='coerce').fillna(0)
        df = df.groupby('name', as_index=False)['student_count'].sum()
        figs['students_by_form'] = bar_chart(
            x=df['name'], y=df['student_count'],
            title='Кількість студентів по класах',
            x_label='Клас', y_label='Студентів'
        )

    # 2. Книги по класах (Pie)
    df = data['books_per_form'].copy()
    if not df.empty and {'name', 'books_count'}.issubset(df.columns):
        df['name'] = df['name'].astype(str)
        df['books_count'] = pd.to_numeric(df['books_count'], errors='coerce').fillna(0)
        df = df.groupby('name', as_index=False)['books_count'].sum()
        figs['books_per_form'] = pie_chart(
            labels=df['name'], values=df['books_count'],
            title='Кількість книг по класах'
        )

    # 3. Ризикові студенти
    df = data['risky_students_attendance'].copy()
    if not df.empty and {'surname', 'missed_lessons'}.issubset(df.columns):
        df['surname'] = df['surname'].astype(str)
        df['missed_lessons'] = pd.to_numeric(df['missed_lessons'], errors='coerce').fillna(0)
        df = df.groupby('surname', as_index=False)['missed_lessons'].sum()
        figs['risky_students'] = bar_chart(
            x=df['surname'], y=df['missed_lessons'],
            title='Пропущені уроки студентами',
            x_label='Студент', y_label='Пропущено', color="#e84d60"
        )

    # 4. Батьки з пільговими дітьми
    df = data['parent_children_by_privilege'].copy()
    if not df.empty and {'surname', 'privileged_children'}.issubset(df.columns):
        df['surname'] = df['surname'].astype(str)
        df['privileged_children'] = pd.to_numeric(df['privileged_children'], errors='coerce').fillna(0)
        df = df.groupby('surname', as_index=False)['privileged_children'].sum()
        figs['privileged_children'] = bar_chart(
            x=df['surname'], y=df['privileged_children'],
            title='Батьки з пільговими дітьми',
            x_label='Батько/Мати', y_label='К-сть дітей', color="#66c2a5"
        )

    # 5. Привілейовані студенти по формах
    df = data['privileged_students_per_form'].copy()
    if not df.empty and {'name', 'privileged_students'}.issubset(df.columns):
        df['name'] = df['name'].astype(str)
        df['privileged_students'] = pd.to_numeric(df['privileged_students'], errors='coerce').fillna(0)
        df = df.groupby('name', as_index=False)['privileged_students'].sum()
        figs['privileged_students'] = bar_chart(
            x=df['name'], y=df['privileged_students'],
            title='Привілейовані студенти по формах',
            x_label='Клас', y_label='Студентів', color="#ddb7b1"
        )

    # 6. Книги на студента
    df = data['books_per_student'].copy()
    if not df.empty and {'surname', 'books_count'}.issubset(df.columns):
        df['surname'] = df['surname'].astype(str)
        df['books_count'] = pd.to_numeric(df['books_count'], errors='coerce').fillna(0)
        df = df.groupby('surname', as_index=False)['books_count'].sum()
        figs['books_per_student'] = bar_chart(
            x=df['surname'], y=df['books_count'],
            title='Кількість книг на студента',
            x_label='Студент', y_label='Книг', color="#c9d9d3"
        )

    # 7. Ризикові студенти по днях (Line)
    df = data['risky_students_per_day'].copy()
    if not df.empty and {'date', 'risky_count'}.issubset(df.columns):
        df['date'] = pd.to_datetime(df['date'], errors='coerce')
        df['risky_count'] = pd.to_numeric(df['risky_count'], errors='coerce').fillna(0)
        df = df.dropna(subset=['date']).groupby('date', as_index=False)['risky_count'].sum()
        figs['risky_students_per_day_line'] = line_chart(
            x=df['date'], y=df['risky_count'],
            title='Кількість ризикових студентів по днях',
            x_label='Дата', y_label='Кількість'
        )

    return figs

