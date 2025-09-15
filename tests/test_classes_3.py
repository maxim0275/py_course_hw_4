import unittest

from src.classes import Category, LawnGrass, Smartphone


class TestProductMethods(unittest.TestCase):

    def setUp(self):
        """Инициализация объектов для тестов"""
        self.smartphone = Smartphone(
            name="iPhone 13",
            description="Latest model",
            price=799.99,
            quantity=10,
            efficiency="High",
            model="A2567",
            memory="128GB",
            color="Black",
        )

        self.lawn_grass = LawnGrass(
            name="Premium Lawn Grass",
            description="High quality lawn grass",
            price=19.99,
            quantity=50,
            country="Germany",
            germination_period="7-14 days",
            color="Green",
        )

        self.category = Category(name="Electronics", description="Various electronic devices")

        self.garden_category = Category(name="Gardening", description="Products for gardening")

    def test_smartphone_initialization(self):
        """Проверка корректной инициализации объекта Smartphone"""
        self.assertEqual(self.smartphone.name, "iPhone 13")
        self.assertEqual(self.smartphone.price, 799.99)
        self.assertEqual(self.smartphone.quantity, 10)

    def test_lawngrass_initialization(self):
        """Проверка корректной инициализации объекта LawnGrass"""
        self.assertEqual(self.lawn_grass.name, "Premium Lawn Grass")
        self.assertEqual(self.lawn_grass.price, 19.99)
        self.assertEqual(self.lawn_grass.quantity, 50)

    def test_add_product_valid(self):
        """Проверка добавления корректных продуктов в категорию"""
        self.category.add_product(self.smartphone)
        self.assertIn(self.smartphone, self.category._Category__products)

    def test_add_product_invalid(self):
        """Проверка ошибки добавления некорректных объектов в категорию"""
        with self.assertRaises(TypeError):
            self.category.add_product("This is not a Product")

    def test_category_str(self):
        """Проверка строкового представления категории"""
        self.assertEqual(str(self.category), "Electronics, количество продуктов: 0 шт.")
        self.category.add_product(self.smartphone)
        self.assertEqual(str(self.category), "Electronics, количество продуктов: 10 шт.")

    def test_iter_category(self):
        """Проверка работы итератора для категории"""
        self.category.add_product(self.smartphone)
        self.garden_category.add_product(self.lawn_grass)
        products = list(iter(self.category))
        garden_products = list(iter(self.garden_category))
        self.assertEqual(products, [self.smartphone])
        self.assertEqual(garden_products, [self.lawn_grass])


if __name__ == "__main__":
    unittest.main()
