from .base_repo import BaseRepository
from main.models import Classroom

class ClassroomRepository(BaseRepository):
    def __init__(self):
        super().__init__(Classroom)
