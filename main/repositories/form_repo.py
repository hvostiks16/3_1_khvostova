from .base_repo import BaseRepository
from main.models import Form

class FormRepository(BaseRepository):
    def __init__(self):
        super().__init__(Form)