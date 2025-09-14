import unittest
from io import StringIO
from unittest.mock import patch

from src.classes import Category, Product


class TestProduct(unittest.TestCase):

    def setUp(self):
        """Очистка экземпляров перед каждым тестом."""
        Product.instances = []

    def test_product_creation(self):
        """test_product_creation: Проверяет правильное создание товара."""
        product = Product("Товар1", "Описание", 100.0, 10)
        self.assertEqual(product.name, "Товар1")
        self.assertEqual(product.description, "Описание")
        self.assertEqual(product.price, 100.0)
        self.assertEqual(product.quantity, 10)
        self.assertEqual(len(Product.instances), 1)

    def test_price_setter(self):
        """test_price_setter: Валидирует корректную работу сеттера цены."""
        product = Product("Товар1", "Описание", 100.0, 10)

        # Check error for negative price
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            product.price = -50.0
            self.assertIn("Цена не должна быть нулевая или отрицательная", mock_stdout.getvalue())

        # Test price confirmation
        with patch("builtins.input", return_value="n"):
            product.price = 90.0
            self.assertEqual(product.price, 100.0)  # Price should remain unchanged

        with patch("builtins.input", return_value="y"):
            product.price = 90.0
            self.assertEqual(product.price, 90.0)  # Price should be changed to 90.0

    def test_new_product(self):
        """test_new_product: Проверяет корректную работу метода new_product."""
        product_data = {"name": "Товар2", "description": "Описание 2", "price": 150.0, "quantity": 5}
        Product.new_product(product_data)
        self.assertEqual(len(Product.instances), 1)

        # Testing if quantity updates when product already exists
        Product.new_product(product_data)
        self.assertEqual(Product.instances[0].quantity, 10)

    def test_product_addition(self):
        """test_product_addition: Проверяет реализацию метода сложения товаров."""
        product1 = Product("Товар1", "Описание1", 50.0, 2)
        product2 = Product("Товар2", "Описание2", 100.0, 3)
        total_value = product1 + product2
        self.assertEqual(total_value, 400.0)

    def test_product_str_repr(self):
        product = Product("Товар1", "Описание", 100.0, 10)
        self.assertEqual(str(product), "Товар1, 100.0 руб. Остаток: 10 шт.")
        self.assertEqual(repr(product), "Product(name=Товар1, price=100.0, quantity=10)")


class TestCategory(unittest.TestCase):
    """setUp: Инициализация счетчиков категории и товаров."""

    def setUp(self):
        Category.product_count = 0
        Category.category_count = 0

    def test_category_creation(self):
        """test_category_creation: Проверяет создание категории."""
        category = Category("Категория 1", "Описание категории")
        self.assertEqual(category.name, "Категория 1")
        self.assertEqual(category.description, "Описание категории")
        self.assertEqual(len(category.products_list), 0)
        self.assertEqual(Category.category_count, 1)

    def test_add_product(self):
        """test_add_product: Проверяет добавление товара в категорию."""
        category = Category("Категория 1", "Описание категории")
        product = Product("Товар1", "Описание", 100.0, 10)
        category.add_product(product)

        self.assertEqual(len(category.products_list), 1)
        self.assertEqual(Category.product_count, 1)

    def test_category_str_repr(self):
        """test_category_str_repr: Проверяет строковое и представленного представления объекта категории."""
        category = Category("Категория 1", "Описание категории")
        self.assertEqual(str(category), "Категория 1, количество продуктов: 0 шт.")
        self.assertEqual(repr(category), "Category(name=Категория 1, products_count=0)")


if __name__ == "__main__":
    unittest.main()
