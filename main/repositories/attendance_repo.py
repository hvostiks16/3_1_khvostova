from .base_repo import BaseRepository
from main.models import Attendance

class AttendanceRepository(BaseRepository):
    def __init__(self):
        super().__init__(Attendance)

