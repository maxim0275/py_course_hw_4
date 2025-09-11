from src.classes import Category, Product  # Замените your_module на имя вашего модуля


def test_product_initialization():
    # Тестирование создания объектов Product
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    assert product1.name == "Samsung Galaxy S23 Ultra"
    assert product1.description == "256GB, Серый цвет, 200MP камера"
    assert product1.price == 180000.0
    assert product1.quantity == 5

    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    assert product2.name == "Iphone 15"
    assert product2.description == "512GB, Gray space"
    assert product2.price == 210000.0
    assert product2.quantity == 8

    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    assert product3.name == "Xiaomi Redmi Note 11"
    assert product3.description == "1024GB, Синий"
    assert product3.price == 31000.0
    assert product3.quantity == 14


def test_category_initialization():
    # Тестирование создания объектов Category и подсчета продуктов
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    assert category1.name == "Смартфоны"
    assert category1.description == (
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert len(category1.products) == 3
    assert category1.products == [product1, product2, product3]


def test_category_counters():
    # Очистка счетчиков перед началом теста
    Category.category_count = 0
    Category.product_count = 0

    product1 = Product("Example Product", "Description", 800.0, 5)
    Category("TestCategory", "TestDescription", [product1])

    assert Category.category_count == 1
    assert Category.product_count == 1

    # Создаем еще одну категорию для проверки
    product2 = Product("New Product", "New Desc", 1200.0, 10)
    category2 = Category("New Category", "Another Description", [product2])

    # Подтверждаем счетчики
    assert Category.category_count == 2
    assert len(category2.products) == 1


def test_repr():
    # Проверка строкового представления объектов
    product = Product("Example", "Sample description", 500.0, 10)
    category = Category("ExampleCategory", "Sample", [product])

    assert repr(product) == "Product(name=Example, price=500.0, quantity=10)"
    assert repr(category) == "Category(name=ExampleCategory, products_count=1)"
