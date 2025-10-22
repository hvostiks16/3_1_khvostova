from .base_repo import BaseRepository
from main.models import BookHasStudent

class BookHasStudentRepository(BaseRepository):
    def __init__(self):
        super().__init__(BookHasStudent)
