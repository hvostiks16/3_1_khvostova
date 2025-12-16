from django.db.models import Count, Q, Sum
from lyceum.models import Attendance, Parent, Student, Form

class AnalyticsRepository:

    @staticmethod
    def students_count_by_form():
        return (
            Form.objects
            .annotate(student_count=Count('students'))        # GROUP BY
            .filter(student_count__gt=0)                     # HAVING
            .values('idClass', 'name', 'student_count')
            .order_by('-student_count')
        )

    @staticmethod
    def books_per_form():
        return (
            Form.objects
            .annotate(
                books_count=Count('students__books', distinct=True)
            )
            .filter(books_count__gt=0)
            .values('name', 'books_count')
            .order_by('-books_count')
        )

    @staticmethod
    def parent_children_by_privilege():
        return (
            Parent.objects
            .annotate(
                privileged_children=Count(
                    'children',
                    filter=Q(
                        children__privilege__in=[
                            'ORPHAN',
                            'LOWINCOME',
                            'DISABLED',
                            'WARVETERANCHILD'
                        ]
                    )
                )
            )
            .filter(privileged_children__gt=0)
            .values(
                'surname',
                'name',
                'privileged_children'
            )
            .order_by('-privileged_children')
        )

    @staticmethod
    def risky_students_attendance():
        return (
            Student.objects
            .values(
                'surname',
                'name',
                'id_form__name'
            )
            .annotate(
                total_lessons=Sum('attendance__amount_of_lessons'),
                missed_lessons=Sum(
                    'attendance__amount_of_lessons',
                    filter=Q(attendance__status='UNAVAILABLE')
                )
            )
            .filter(
                missed_lessons__gt=5                              # замість .having()
            )
            .order_by('-missed_lessons')
        )

    @staticmethod
    def privileged_students_per_form():
        return (
            Form.objects
            .annotate(
                privileged_students=Count(
                    'students',
                    filter=Q(students__privilege__in=[
                        'ORPHAN', 'LOWINCOME', 'DISABLED', 'WARVETERANCHILD'
                    ])
                )
            )
            .filter(privileged_students__gt=0)
            .values('name', 'privileged_students')
            .order_by('-privileged_students')
        )

    @staticmethod
    def books_per_student():
        return (
            Student.objects
            .annotate(books_count=Count('books', distinct=True))
            .filter(books_count__gt=0)
            .values('surname', 'name', 'books_count')
            .order_by('-books_count')
        )

    @staticmethod
    def risky_students_per_day():
        return (
            Attendance.objects
            .values('date')
            .annotate(
                risky_count=Count(
                    'id_student',
                    filter=Q(status='UNAVAILABLE') & Q(amount_of_lessons__gt=5),
                    distinct=True
                )
            )
            .order_by('date')
        )