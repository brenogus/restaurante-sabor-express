from abc import ABC, abstractmethod
class ItemCardapio(ABC):
    def __init__(self,item: dict):
        self._item = item['item']
        self._price = item['price']
        self._description = item['description']

    def __str__(self):
        return f'{self._item.ljust(40)} | {str(self._price).ljust(40)} | {self._description.ljust(40)}'

    