from django.urls import path
from . import views
from lyceum.dashboard.views import dashboard, dashboard_bokeh
from lyceum.api_views import (
    FormsStudentsCountAPI,
    BooksPerFormAPI,
    ParentChildrenByPrivilegeAPI,
    RiskyStudentsAttendanceAPI,
    PrivilegedStudentsPerFormAPI,
    BooksPerStudentAPI,
    StudentAgeStatsAPI,
    ClassroomCapacityStatsAPI,
    AverageAgePerFormAPI,
    AverageAgeByPrivilegeAPI,
    MaxBooksPerStudentPerFormAPI,
    RiskyStudentsPerDayAPI,
)
from lyceum.parallel.views import parallel_dashboard

urlpatterns = [
    path("parallel/", parallel_dashboard, name="parallel"),
    path('dashboard/', dashboard, name='dashboard'),
    path('dashboard_bokeh/', dashboard_bokeh, name='dashboard_bokeh'),

    path('analytics/forms-students-count/', FormsStudentsCountAPI.as_view(), name='analytics_forms_students_count'),
    path('analytics/books-per-form/', BooksPerFormAPI.as_view(), name='books-per-form'),
    path('analytics/parents-children-by-privilege/', ParentChildrenByPrivilegeAPI.as_view(), name='analytics_parents_children_by_privilege'),
    path('analytics/risky-students-attendance/', RiskyStudentsAttendanceAPI.as_view(), name='analytics_risky_students_attendance'),
    path('analytics/privileged-students-per-form/', PrivilegedStudentsPerFormAPI.as_view(), name='analytics_privileged_students_per_form'),
    path('analytics/books-per-student/', BooksPerStudentAPI.as_view(), name='analytics_books_per_student'),
    path('analytics/risky-students-per-day/', RiskyStudentsPerDayAPI.as_view(), name='risky_students_per_day_api'),

    path('statistics/student-age/', StudentAgeStatsAPI.as_view(), name='student-age-stats'),
    path('statistics/classroom-capacity/', ClassroomCapacityStatsAPI.as_view(), name='classroom-capacity-stats'),
    path('statistics/average-age-per-form/', AverageAgePerFormAPI.as_view(), name='average-age-per-form'),
    path('statistics/average-age-by-privilege/', AverageAgeByPrivilegeAPI.as_view(), name='average-age-by-privilege'),
    path('statistics/max-books-per-student-per-form/', MaxBooksPerStudentPerFormAPI.as_view(), name='max-books-per-student-per-form'),

    path("gids/", views.gid_list, name="gid_list"),
    path("tours/", views.tour_list, name="tour_list"),
    #TEACHER
    path('teachers/', views.teacher_list, name='teacher_list'),
    path('teachers/create/', views.teacher_create, name='teacher_create'),
    path('teachers/<int:pk>/', views.teacher_detail, name='teacher_detail'),
    path('teachers/<int:pk>/edit/', views.teacher_update, name='teacher_update'),
    path('teachers/<int:pk>/delete/', views.teacher_delete, name='teacher_delete'),

# STUDENT
    path('students/', views.student_list, name='student_list'),
    path('students/create/', views.student_create, name='student_create'),
    path('students/<int:pk>/', views.student_detail, name='student_detail'),
    path('students/<int:pk>/edit/', views.student_update, name='student_update'),
    path('students/<int:pk>/delete/', views.student_delete, name='student_delete'),

    # PARENT
    path('parents/', views.parent_list, name='parent_list'),
    path('parents/create/', views.parent_create, name='parent_create'),
    path('parents/<int:pk>/', views.parent_detail, name='parent_detail'),
    path('parents/<int:pk>/edit/', views.parent_update, name='parent_update'),
    path('parents/<int:pk>/delete/', views.parent_delete, name='parent_delete'),
]
