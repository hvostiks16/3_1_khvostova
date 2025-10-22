from .base_repo import BaseRepository
from main.models import Schedule

class ScheduleRepository(BaseRepository):
    def __init__(self):
        super().__init__(Schedule)
