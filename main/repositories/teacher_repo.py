from .base_repo import BaseRepository
from main.models import Teacher

class TeacherRepository(BaseRepository):
    def __init__(self):
        super().__init__(Teacher)
