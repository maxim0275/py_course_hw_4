class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"Product(name={self.name}, price={self.price}, quantity={self.quantity})"


class Category:
    # Атрибуты класса для хранения количества категорий и товаров
    category_count = 0
    total_product_count = 0

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.products = []

        # Увеличиваем счётчик количества категорий при создании нового объекта
        Category.category_count += 1

    def add_product(self, product: Product):
        self.products.append(product)
        # Увеличиваем общий счётчик количества товаров
        Category.total_product_count += 1

    def __repr__(self):
        return f"Category(name={self.name}, products_count={len(self.products)})"