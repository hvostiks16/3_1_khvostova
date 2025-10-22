from .base_repo import BaseRepository
from main.models import Student

class StudentRepository(BaseRepository):
    def __init__(self):
        super().__init__(Student)
