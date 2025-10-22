class BaseRepository:
    def __init__(self, model):
        self._model = model

    def get_all(self):
        return self._model.objects.all()

    def get_by_id(self, obj_id):
        pk_field = self._model._meta.pk.name
        return self._model.objects.get(**{pk_field: obj_id})

    def add(self, data):
        try:
            if self._model.objects.filter(**data).exists():
                print(f"Запис уже існує: {data}")
                return None
            return self._model.objects.create(**data)
        except Exception as e:
            print(f"Помилка при додаванні: {e}")
            return None

    @staticmethod
    def description():
        return "Базовий репозиторій для доступу до сутностей БД"
