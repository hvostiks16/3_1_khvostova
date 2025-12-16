from django.shortcuts import render
from .dashboard_plotly import dashboard_plotly_components
from .dashboard_bokeh import dashboard_bokeh_components
import json
# def dashboard(request):
#     figs = dashboard_plotly_components()
#     return render(request, 'lyceum/dashboard.html', {'figs': figs})


def dashboard(request):
    figs = dashboard_plotly_components()
    # серіалізація у JSON (plain dict з data/layout)
    figs_json = json.dumps(figs, default=str)  # default=str для дат
    return render(request, 'lyceum/dashboard.html', {'figs_json': figs_json})
def dashboard_bokeh(request):
    figs = dashboard_bokeh_components()
    return render(request, 'lyceum/dashboard_bokeh.html', {'figs': figs})
