import pytest

from shop.models import Category, Product


def test_product_initialization():
    product = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    assert product.name == "Iphone 15"
    assert product.description == "512GB, Gray space"
    assert product.price == 210000.0
    assert product.quantity == 8


def test_category_initialization():
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    category = Category("Смартфоны", "Категория смартфонов", [product1, product2])
    assert category.name == "Смартфоны"
    assert category.product_count == 2
    assert category.category_count >= 1  # Потому что могли быть созданы другие категории


def test_category_count():
    assert Category.category_count > 0


def test_product_count():
    assert Category.product_count > 0
