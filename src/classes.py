from src.base_order_category import Base_Ord_Cat
from src.base_product import BaseProduct
from src.mixin_print import MixinPrint


class Product(MixinPrint, BaseProduct):
    instances = []

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        self.instances.append(self)
        super().__init__()

    @property
    def price(self):
        """Геттер для цены"""
        return self.__price

    @price.setter
    def price(self, value: float):
        """Сеттер для цены с проверкой и подтверждением снижения цены"""
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif value < self.__price:
            response = input("Цена снижена. Подтвердите изменение (y/n): ")
            if response.lower() == "y":
                self.__price = value
            else:
                print("Изменение цены отменено.")
        else:
            self.__price = value

    @classmethod
    def new_product(cls, product_data: dict):
        for product in Product.instances:
            if product.name == product_data.get("name", ""):
                product.quantity += product_data.get("quantity", 0)
                product.price = max(product.price, product_data.get("price", 0.0))
                return product

        return cls(
            name=product_data.get("name", ""),
            description=product_data.get("description", ""),
            price=product_data.get("price", 0.0),
            quantity=product_data.get("quantity", 0),
        )

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if not isinstance(other, Product):
            return NotImplemented
        if type(self) is not type(other):
            raise TypeError(f"Нельзя сложить {type(self).__name__} и {type(other).__name__}")
        return self.price * self.quantity + other.price * other.quantity


class Category:
    product_count = 0
    category_count = 0

    def __init__(self, name: str, description: str, products=None):
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(self.__products)

    def add_product(self, new_product):
        if not isinstance(new_product, Product):
            raise TypeError("Можно добавлять только объекты Product или его подклассов.")

        self.__products.append(new_product)
        Category.product_count += 1

    @property
    def products(self):
        """Геттер, возвращающий строковое представление списка товаров"""
        return "\n".join(str(product) for product in self.__products)

    @property
    def products_list(self):
        """Геттер, возвращающий список товаров"""
        return [str(product) for product in self.__products]

    def __repr__(self):
        return f"Category(name={self.name}, products_count={len(self.__products)})"

    def __str__(self):
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def __iter__(self):
        return CategoryIterator(self)


# * Дополнительное задание
class CategoryIterator:
    """Принимает объект категории в конструкторе. Инициализирует индекс,
    который будет использоваться для отслеживания текущей позиции в списке товаров."""

    def __init__(self, category):
        self._category = category
        self._index = 0

    def __iter__(self):
        """Возвращает сам объект итератора (в данном случае возвращает объект CategoryIterator)"""
        return self

    def __next__(self):
        """Возвращает следующий товар в категории. Если товары закончились,
        вызывает StopIteration для завершения итерации."""
        if self._index < len(self._category.products_list):
            product = self._category._Category__products[self._index]
            self._index += 1
            return product
        else:
            raise StopIteration


# ==================== подклассы


class Smartphone(Product):
    """Подкласс Смартфон"""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: str,
        model: str,
        memory: str,
        color: str,
    ):
        """Новый конструктор"""
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color
        super().__init__(name, description, price, quantity)

    def __repr__(self):
        """Изменить представление для отладки"""
        return (
            f"Smartphone(name={self.name}, model={self.model}, price={self.price}, "
            f"quantity={self.quantity}, efficiency={self.efficiency}, memory={self.memory}, color={self.color})"
        )

    def __str__(self):
        """Изменить представление для пользователя"""
        return (
            f"{self.name} (модель {self.model}), {self.price} руб. "
            f"Остаток: {self.quantity} шт., цвет: {self.color}, "
            f"производительность: {self.efficiency}, память: {self.memory}"
        )


class LawnGrass(Product):
    """Подскласс трава газонная"""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ):
        """Новый конструктор"""

        self.country = country
        self.germination_period = germination_period
        self.color = color
        super().__init__(name, description, price, quantity)

    def __repr__(self):
        """Изменить представление для отладки"""
        return (
            f"LawnGrass(name={self.name}, country={self.country}, price={self.price}, "
            f"quantity={self.quantity}, germination_period={self.germination_period}, color={self.color})"
        )

    def __str__(self):
        """Изменить представление для пользователя"""
        return (
            f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт., "
            f"страна-производитель: {self.country}, срок прорастания: {self.germination_period}, цвет: {self.color}"
        )


class Order(Base_Ord_Cat):
    """Класс Заказ"""

    def __init__(self, name: str, description, product: Product, quantity: int):
        super().__init__()
        self.name = name
        self.description = description
        self.product = product
        self.quantity = quantity

    @property
    def total_cost(self):
        """Стоимость заказа"""
        return self.quantity * self.product.price

    @property
    def products(self):
        return self.product

    def __repr__(self):
        return (
            f" Имя заказа: {self.name}, Описание заказа: {self.description}, "
            f"Продукт: {self.product}, Количество: {self.quantity}, "
            f"Цена: {self.product.price}, Стоимость:{self.total_cost}"
        )
