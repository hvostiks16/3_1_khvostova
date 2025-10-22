from main.repositories import (
    AttendanceRepository, BookRepository, ClassroomRepository, ParentRepository,
    BookHasStudentRepository, FormRepository, StudentRepository,
    TeacherRepository, ScheduleRepository
)

class UnitOfWork:
    def __init__(self):
        self.books = BookRepository()
        self.attendances = AttendanceRepository()
        self.classes = ClassroomRepository()
        self.parents = ParentRepository()
        self.forms = FormRepository()
        self.students = StudentRepository()
        self.teachers = TeacherRepository()
        self.schedules = ScheduleRepository()
        self.books_have_students = BookHasStudentRepository()
