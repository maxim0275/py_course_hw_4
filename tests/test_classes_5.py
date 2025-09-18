import unittest

from src.classes import Category, Product


class TestProductMethods(unittest.TestCase):

    def setUp(self):
        self.product1 = Product("Мотоцикл Урал", "Мотоцикл Урал 76 л/с", 50000, 1)
        self.product2 = Product("Мотоцикл Иэ Юпитер", "Мотоцикл Иэ Юпитер 60 л/с", 60000, 1)

        self.cat_moto = Category("Мотоциклы", "Категория мототехники", [self.product1, self.product2])
        self.cat_auto = Category("Автомобили", "Категория автомобилей", [])

    def test_middle_price(self):
        self.assertEqual(self.cat_moto.middle_price(), 55000)
        self.assertEqual(self.cat_auto.middle_price(), 0)
