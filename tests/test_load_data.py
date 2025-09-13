import json

import pytest

from src.classes import Category, Product
from src.load_data import load_data_from_json

# Создаем фиктивные JSON данные для тестирования
mock_json_data = json.dumps(
    [
        {
            "name": "Телефоны",
            "description": "Электронные устройства",
            "products": [
                {"name": "Xiaomi Mi 11", "description": "128GB, Черный цвет", "price": 45000.0, "quantity": 10}
            ],
        }
    ]
)


@pytest.fixture
def mock_json_file(tmp_path):
    # Создать временный файл с фиктивными данными
    file_path = tmp_path / "mock_data.json"
    file_path.write_text(mock_json_data, encoding="utf-8")
    return str(file_path)


def test_load_data_from_json(mock_json_file):
    categories = load_data_from_json(mock_json_file)

    assert len(categories) == 1
    category = categories[0]
    assert category.name == "Телефоны"
    assert category.description == "Электронные устройства"
    assert len(category.products) == 1

    product = category.products[0]
    assert "Xiaomi Mi 11" in product
    assert "45000.0" in product
    assert "10" in product


def test_product_initialization():
    product = Product(name="Test Product", description="Test Description", price=100.0, quantity=5)
    assert product.name == "Test Product"
    assert product.description == "Test Description"
    assert product.price == 100.0
    assert product.quantity == 5


def test_category_initialization():
    product = Product(name="Test Product", description="Test Description", price=100.0, quantity=5)
    category = Category(name="Test Category", description="Test Category Description", products=[product])
    assert category.name == "Test Category"
    assert category.description == "Test Category Description"
    assert len(category.products) == 1
    assert product.name in category.products[0]
