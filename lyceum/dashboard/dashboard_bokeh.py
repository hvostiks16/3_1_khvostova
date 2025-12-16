import pandas as pd
from math import pi
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.transform import cumsum
from bokeh.models import ColumnDataSource, FactorRange, Range1d
from bokeh.palettes import Category20c
from .dashboard_data import get_dashboard_data

def dashboard_bokeh_components():
    data = get_dashboard_data()
    components_dict = {}

    # 1. Студенти по класах
    df = data['students_count_by_form']
    if df.empty:
        p = figure(title="Немає даних", height=300)
    else:
        source = ColumnDataSource(df)
        p = figure(x_range=df['name'].tolist(), title="Кількість студентів по класах", height=400)
        p.vbar(x='name', top='student_count', width=0.9, source=source)
        p.xgrid.grid_line_color = None
        p.y_range.start = 0
    components_dict['students_by_form'] = components(p)

    # 2. Pie: книги по класах
    df = data['books_per_form']
    if df.empty:
        p = figure(title="Немає даних", height=300)
    else:
        df['angle'] = df['books_count']/df['books_count'].sum() * 2*pi
        df['color'] = Category20c[len(df)]
        source = ColumnDataSource(df)
        p = figure(title="Кількість книг по класах", x_range=Range1d(-1, 1), y_range=Range1d(-1, 1), height=400)
        p.wedge(x=0, y=0, radius=0.4,
                start_angle=cumsum('angle', include_zero=True),
                end_angle=cumsum('angle'),
                line_color="white", fill_color='color',
                legend_field='name', source=source)
        p.axis.visible = False
        p.grid.visible = False
    components_dict['books_per_form'] = components(p)

    # 3. Ризикові студенти
    df = data['risky_students_attendance']
    if df.empty:
        p = figure(title="Немає даних", height=300)
    else:
        source = ColumnDataSource(df)
        p = figure(x_range=df['surname'].tolist(), title="Пропущені уроки студентами", height=400)
        p.vbar(x='surname', top='missed_lessons', width=0.9, source=source, color="#e84d60")
        p.xgrid.grid_line_color = None
        p.y_range.start = 0
    components_dict['risky_students'] = components(p)

    # 4. Батьки з пільговими дітьми
    df = data['parent_children_by_privilege']
    if df.empty:
        p = figure(title="Немає даних", height=300)
    else:
        source = ColumnDataSource(df)
        p = figure(x_range=df['surname'].tolist(), title="Батьки з пільговими дітьми", height=400)
        p.vbar(x='surname', top='privileged_children', width=0.9, source=source, color="#66c2a5")
        p.xgrid.grid_line_color = None
        p.y_range.start = 0
    components_dict['privileged_children'] = components(p)

    # 5. Привілейовані студенти по формах
    df = data['privileged_students_per_form']
    if df.empty:
        p = figure(title="Немає даних", height=300)
    else:
        source = ColumnDataSource(df)
        p = figure(x_range=df['name'].tolist(), title="Привілейовані студенти по формах", height=400)
        p.vbar(x='name', top='privileged_students', width=0.9, source=source, color="#ddb7b1")
        p.xgrid.grid_line_color = None
        p.y_range.start = 0
    components_dict['privileged_students'] = components(p)

    # 6. Книги на студента
    df = data['books_per_student']
    if df.empty:
        p = figure(title="Немає даних", height=300)
    else:
        source = ColumnDataSource(df)
        p = figure(x_range=df['surname'].tolist(), title="Кількість книг на студента", height=400)
        p.vbar(x='surname', top='books_count', width=0.9, source=source, color="#c9d9d3")
        p.xgrid.grid_line_color = None
        p.y_range.start = 0
    components_dict['books_per_student'] = components(p)

    # 7. Ризикові студенти по днях
    df = data['risky_students_per_day']
    if df.empty:
        p = figure(title="Немає даних", height=300)
    else:
        source = ColumnDataSource(df)
        p = figure(title="Кількість ризикових студентів по днях", x_axis_type="datetime", height=400)
        p.line(x='date', y='risky_count', source=source, line_width=2)
        p.scatter(x='date', y='risky_count', source=source, size=8)
    components_dict['risky_students_per_day_line'] = components(p)

    return components_dict
