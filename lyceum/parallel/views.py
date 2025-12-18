import time
import random
import pandas as pd
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed
from django.db import connection
from django.shortcuts import render
import plotly.graph_objects as go

#одиночний запит
def run_single_query(_=None):
    start = time.perf_counter()
    time.sleep(random.uniform(0.01, 0.05))
    with connection.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) FROM Book WHERE Status = 'BORROWED';")
        cursor.fetchone()
    return time.perf_counter() - start

#загальна функція тестування
def run_parallel_tests(workers_list=None, total_queries=100, mode="thread"):
    results = []

    if workers_list is None:
        workers_list = [1, 2, 4, 8, 16]

    for workers in workers_list:
        max_workers = min(workers, total_queries, 10)
        start_total = time.perf_counter()
        durations = []

        if mode == "thread":
            ExecutorClass = ThreadPoolExecutor
        elif mode == "process":
            ExecutorClass = ProcessPoolExecutor
        else:
            raise ValueError("mode must be 'thread' or 'process'")

        with ExecutorClass(max_workers=max_workers) as executor:
            batch_size = max_workers
            for i in range(0, total_queries, batch_size):
                batch_futures = [executor.submit(run_single_query) for _ in range(min(batch_size, total_queries - i))]
                durations.extend([f.result() for f in as_completed(batch_futures)])

        total_time = time.perf_counter() - start_total
        avg_query_time = sum(durations) / len(durations) if durations else 0

        results.append({
            "workers": workers,
            "total_time": total_time,
            "avg_query_time": avg_query_time,
        })

    df = pd.DataFrame(results)
    return df

def parallel_dashboard(request):
    workers_raw = request.GET.get("workers")
    mode = request.GET.get("mode", "thread")  # додали параметр mode

    if workers_raw:
        parts = workers_raw.split(",")
        workers = [int(p) for p in parts]
    else:
        workers = [1, 2, 4, 8, 16]

    df = run_parallel_tests(workers_list=workers, total_queries=100, mode=mode)

    #графік загального часу
    fig_total = go.Figure()
    fig_total.add_trace(go.Scatter(
        x=df['workers'],
        y=df['total_time'],
        mode='lines+markers',
        name=f'Total Time ({mode})'
    ))
    fig_total.update_layout(
        title=f"Execution time for borrowed books query ({mode})",
        xaxis_title="Workers",
        yaxis_title="Time (sec)",
        hovermode="x unified"
    )
    graph_total = fig_total.to_html(full_html=False, include_plotlyjs='cdn')

    #графік середнього часу
    fig_avg = go.Figure()
    fig_avg.add_trace(go.Scatter(
        x=df['workers'],
        y=df['avg_query_time'],
        mode='lines+markers',
        name=f'Avg Query Time ({mode})',
        marker=dict(color='red')
    ))
    fig_avg.update_layout(
        title=f"Average request duration ({mode})",
        xaxis_title="Workers",
        yaxis_title="Average request duration (sec)",
        hovermode="x unified"
    )
    graph_avg = fig_avg.to_html(full_html=False, include_plotlyjs=False)

    return render(
        request,
        "lyceum/parallel.html",
        {
            "graph_total": graph_total,
            "graph_avg": graph_avg,
            "df": df.to_html(classes="table table-striped"),
            "current_workers": workers_raw if workers_raw else ",".join(map(str, workers)),
            "current_mode": mode
        }
    )
