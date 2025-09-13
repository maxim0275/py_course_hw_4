from unittest.mock import patch

from src.classes import Category, Product


def test_product_creation():
    # Создание продукта
    prod = Product("Кофе", "Свежемолотый кофе", 350.0, 100)
    assert prod.name == "Кофе"
    assert prod.description == "Свежемолотый кофе"
    assert prod.price == 350.0
    assert prod.quantity == 100
    print("test_product_creation passed")


def test_product_price_update():
    # Создание продукта
    prod = Product("Чай", "Черный чай", 150.0, 50)
    # Изменение цены
    prod.price = 175.0
    assert prod.price == 175.0
    print("test_product_price_update passed")


def test_product_price_decrease_confirmation():
    # Создание продукта
    prod = Product("Сахар", "Белый сахар", 50.0, 20)

    # Используем patch для замены input
    with patch("builtins.input", return_value="y"):
        prod.price = 45.0

    assert prod.price == 45.0
    print("test_product_price_decrease_confirmation passed")


def test_new_product_classmethod():
    # Добавление нового продукта через classmethod
    product_data = {"name": "Молоко", "description": "Пастеризованное", "price": 60.0, "quantity": 30}
    new_prod = Product.new_product(product_data)
    assert new_prod.name == "Молоко"
    assert new_prod.price == 60.0
    assert new_prod.quantity == 30

    # Обновление существующего продукта
    updated_data = {"name": "Молоко", "price": 65.0, "quantity": 20}
    updated_prod = Product.new_product(updated_data)
    assert updated_prod.quantity == 50  # 30 + 20
    assert updated_prod.price == 65.0

    print("test_new_product_classmethod passed")


def test_category_creation():
    # Создание категории с продуктами
    prod1 = Product("Хлеб", "Свежий хлеб", 30.0, 20)
    prod2 = Product("Масло", "Масло сливочное", 100.0, 10)
    category = Category("Продукты питания", "Основные продукты", [prod1, prod2])

    assert category.name == "Продукты питания"
    assert Category.category_count == 1
    assert Category.product_count == 2
    print("test_category_creation passed")


def test_category_add_product():
    # Добавление продукта в категорию
    category = Category("Напитки", "Напитки всех видов")
    prod = Product("Кока-кола", "Газированный напиток", 50.0, 15)
    category.add_product(prod)

    assert len(category.products) == 1
    assert Category.product_count == 3
    print("test_category_add_product passed")
