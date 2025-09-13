from src.classes import Category, Product  # Замените your_module на имя вашего модуля, где определены классы


def test_product_initialization():
    # Проверка корректности инициализации продукта
    product = Product("Samsung Galaxy S23", "256GB, Серый", 150000.0, 10)
    assert product.name == "Samsung Galaxy S23"
    assert product.description == "256GB, Серый"
    assert product.price == 150000.0
    assert product.quantity == 10


def test_category_initialization():
    # Проверка корректности инициализации категории
    product1 = Product("Product1", "Description1", 1000.0, 5)
    category = Category("Electronics", "Various electronic products", [product1])

    assert category.name == "Electronics"
    assert category.description == "Various electronic products"
    assert len(category.products) == 1
    assert product1.name in category.products[0]


def test_category_count():
    # Сбросим счетчики перед тестом
    Category.category_count = 0

    # Создание нескольких категорий
    category1 = Category("Category1", "Description1")
    category2 = Category("Category2", "Description2")

    # Проверка реализации строкового представления
    product = Product("Example", "Description", 50.0, 5)
    category1.products.append(product)  # добавляем продукт вручную
    assert repr(category1) == "Category(name=Category1, products_count=0)"
    assert repr(category2) == "Category(name=Category2, products_count=0)"


def test_repr_methods():
    # Проверка строковых представлений объектов
    product = Product("Gadget", "Useful", 299.99, 20)
    category = Category("Gadgets", "Various gadgets", [product])

    assert repr(product) == "Product(name=Gadget, price=299.99, quantity=20)"
    assert repr(category) == "Category(name=Gadgets, products_count=1)"
