class Product:
    instances = []

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        self.instances.append(self)

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

    def __repr__(self):
        return f"Product(name={self.name}, price={self.price}, quantity={self.quantity})"

    # Задание 1
    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    # Задание 2
    def __add__(self, other):
        if not isinstance(other, Product):
            return NotImplemented
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

    def add_product(self, new_product: Product):
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

    # Задание 1
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
