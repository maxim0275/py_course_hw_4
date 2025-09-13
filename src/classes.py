class Product:
    instances = []
    """
    Продукт
    """

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price  # Приватный атрибут для цены
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


class Category:
    product_count = 0
    category_count = 0
    """Категория"""

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
        """Геттер, возвращающий список товаров"""
        # return list(
        #     [f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт." for product in self.__products]
        # )
        return "\n".join(
            [f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт." for product in self.__products]
        )

    @property
    def products_list(self):
        """Геттер, возвращающий список товаров"""
        return list(
            [f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт." for product in self.__products]
        )

    def __repr__(self):
        return f"Category(name={self.name}, products_count={len(self.__products)})"
