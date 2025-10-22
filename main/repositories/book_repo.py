from .base_repo import BaseRepository
from main.models import Book

class BookRepository(BaseRepository):
    def __init__(self):
        super().__init__(Book)

    def get_by_status(self, status: str):
        return self._model.objects.filter(status=status)
