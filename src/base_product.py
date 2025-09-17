from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Базовы класс для класса Product"""

    @classmethod
    @abstractmethod
    def new_product(cls, *args, **kwargs):
        pass
