from main.repositories import (
    AttendanceRepository, BookRepository, ClassroomRepository, ParentRepository,
    FormRepository, StudentRepository,
    TeacherRepository, ScheduleRepository
)

class UnitOfWork:
    def __init__(self):
        self.books = BookRepository()
        self.attendances = AttendanceRepository()
        self.classrooms = ClassroomRepository()
        self.parents = ParentRepository()
        self.forms = FormRepository()
        self.students = StudentRepository()
        self.teachers = TeacherRepository()
        self.schedules = ScheduleRepository()
