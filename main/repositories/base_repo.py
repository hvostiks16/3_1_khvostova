from typing import Any, Dict, Optional

class BaseRepository:
    def __init__(self, model):
        self._model = model

    def get_all(self):
        return self._model.objects.all()

    def get_by_id(self, obj_id):
        pk_field = self._model._meta.pk.name
        return self._model.objects.get(**{pk_field: obj_id})

    def create(self, data: Dict[str, Any]) -> Any:
        return self._model.objects.create(**data)

    def update(self, pk, **kwargs) -> Optional[Any]:
        obj = self.get_by_id(pk)
        if not obj:
            return None
        for k, v in kwargs.items():
            setattr(obj, k, v)
        obj.save()
        return obj

    def delete(self, pk) -> bool:
        obj = self.get_by_id(pk)
        if not obj:
            return False
        obj.delete()
        return True