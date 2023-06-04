from FridgeClass.managers.fridge_manager import FridgeManager


class SetManager:
    """Content of class SetManager."""

    def __init__(self, fridges_manager: FridgeManager):
        self._set = set()
        self._index = 0
        for fridges in fridges_manager:
            self._set.update(fridges.my_special_set)

    def __len__(self):
        return len(self._set)

    def __getitem__(self, index):
        return list(self._set)[index]

    def __iter__(self):
        self._index = 0
        return self

    def __next__(self):
        try:
            item = list(self._set)[self._index]
        except IndexError as exc:
            raise StopIteration() from exc
        self._index += 1
        return item
