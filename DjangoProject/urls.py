from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from main import view
from main.view import StudentsPerClassReportView, AvailableBooksView
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register(r'books', view.BookViewSet)
router.register(r'students', view.StudentViewSet)
router.register(r'classrooms', view.ClassroomViewSet)
router.register(r'forms', view.FormViewSet)
router.register(r'parents', view.ParentViewSet)
router.register(r'schedule', view.ScheduleViewSet)
router.register(r'teachers', view.TeacherViewSet)

urlpatterns = [
    path('api-token-auth/', obtain_auth_token),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/reports/students_per_class/', StudentsPerClassReportView.as_view(), name='students-per-class-report'),
    path('api/reports/available_books/', AvailableBooksView.as_view(), name='available-books'),
    path('lyceum/', include('lyceum.urls')),
]
