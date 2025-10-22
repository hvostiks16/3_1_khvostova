from .base_repo import BaseRepository
from main.models import Parent

class ParentRepository(BaseRepository):
    def __init__(self):
        super().__init__(Parent)
