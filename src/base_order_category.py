from abc import ABC, abstractmethod


class Base_Ord_Cat(ABC):
    """ " Базовый класс для классов Category и Order"""

    def __init__(self):
        pass

    @property
    @abstractmethod
    def products(self):
        pass
