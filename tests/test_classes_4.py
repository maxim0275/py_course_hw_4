import unittest

from src.classes import Product, Smartphone


class TestProductMethods(unittest.TestCase):

    def setUp(self):
        self.product1 = Product("Мотоцикл Урал", "Мотоцикл Урал 76 л/с", 50000, 1)
        self.telephone = Smartphone(
            name="HUAWEI H20PRO",
            description="HUAWEI H20PRO 256MB",
            price=500,
            quantity=11,
            efficiency="High",
            model="H20PRO",
            memory="256GB",
            color="Pink",
        )

    def test_mixin_print(self):
        # print(self.product1.__repr__())
        self.assertEqual(self.product1.__repr__(), "Product(Мотоцикл Урал, Мотоцикл Урал 76 л/с, 50000, 1)")

    def test_super_class(self):
        self.assertIn("Product", self.telephone.__class__.__bases__.__repr__())
