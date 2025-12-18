from django.shortcuts import render
from .dashboard_plotly import dashboard_plotly_components
from .dashboard_bokeh import dashboard_bokeh_components
import json

def dashboard(request):
    filters = {
        'students_sort': request.GET.get('students_sort'),   # asc / desc
        'books_filter': request.GET.get('books_filter'),     # назва класу
    }
    figs = dashboard_plotly_components(filters=filters)
    figs_json = json.dumps(figs, default=str)
    return render(request, 'lyceum/dashboard.html', {
        'figs_json': figs_json,
        'filters': filters
    })

def dashboard_bokeh(request):
    filters = {
        'students_sort': request.GET.get('students_sort'),
    }

    figs = dashboard_bokeh_components(filters=filters)
    return render(request, 'lyceum/dashboard_bokeh.html', {
        'figs': figs
    })
