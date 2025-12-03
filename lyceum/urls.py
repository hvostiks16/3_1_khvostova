from django.urls import path
from . import views

urlpatterns = [
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
