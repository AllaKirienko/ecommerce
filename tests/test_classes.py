from src.ecommerce.classes import Category, Product


def test_product_initialization():
    product = Product(
        name="Телефон",
        description="Смартфон",
        price=50000.0,
        quantity=10,
    )

    assert product.name == "Телефон"
    assert product.description == "Смартфон"
    assert product.price == 50000.0
    assert product.quantity == 10


def test_category_initialization():
    product = Product(
        name="Телефон",
        description="Смартфон",
        price=50000.0,
        quantity=10,
    )

    category = Category(
        name="Электроника",
        description="Техника",
        products=[product],
    )

    assert category.name == "Электроника"
    assert category.description == "Техника"
    assert category.products == [product]


def test_product_count():
    initial_product_count = Category.product_count

    product_1 = Product("Телефон", "Смартфон", 50000.0, 10)
    product_2 = Product("Ноутбук", "Компьютер", 100000.0, 5)

    Category(
        "Электроника",
        "Техника",
        [product_1, product_2],
    )

    assert Category.product_count == initial_product_count + 2


def test_category_count():
    initial_category_count = Category.category_count

    product = Product("Телефон", "Смартфон", 50000.0, 10)

    Category("Электроника", "Техника", [product])
    Category("Бытовая техника", "Техника для дома", [product])

    assert Category.category_count == initial_category_count + 2


def test_product_str():
    product = Product(
        "Телефон",
        "Смартфон",
        50000.0,
        10,
    )

    assert str(product) == "Телефон, 50000.0 руб. Остаток: 10 шт."


def test_category_str():
    product_1 = Product(
        "Телефон",
        "Смартфон",
        50000.0,
        10,
    )

    product_2 = Product(
        "Ноутбук",
        "Компьютер",
        100000.0,
        5,
    )

    category = Category(
        "Электроника",
        "Техника",
        [product_1, product_2],
    )

    assert str(category) == "Электроника, количество продуктов: 15 шт."


def test_product_add():
    product_1 = Product(
        "Телефон",
        "Смартфон",
        50000.0,
        10,
    )

    product_2 = Product(
        "Ноутбук",
        "Компьютер",
        100000.0,
        5,
    )

    assert product_1 + product_2 == 1000000.0
