from src.ecommerce.classes import (
    Category,
    Product,
    Smartphone,
    LawnGrass,
)


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

    expected_product = "Телефон, 50000.0 руб. " "Остаток: 10 шт."

    assert category.name == "Электроника"
    assert category.description == "Техника"
    assert category.products == expected_product


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


def test_add_product():
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
        [product_1],
    )

    initial_count = Category.product_count

    category.add_product(product_2)

    assert "Ноутбук, 100000.0 руб. Остаток: 5 шт." in category.products
    assert Category.product_count == initial_count + 1


def test_product_price_setter():
    product = Product(
        "Телефон",
        "Смартфон",
        50000.0,
        10,
    )

    product.price = 60000.0

    assert product.price == 60000.0


def test_product_negative_price():
    product = Product(
        "Телефон",
        "Смартфон",
        50000.0,
        10,
    )

    product.price = -100

    assert product.price == 50000.0


def test_new_product():
    product_data = {
        "name": "Телефон",
        "description": "Смартфон",
        "price": 50000.0,
        "quantity": 10,
    }

    product = Product.new_product(product_data)

    assert product.name == "Телефон"
    assert product.description == "Смартфон"
    assert product.price == 50000.0
    assert product.quantity == 10


def test_smartphone_initialization():
    smartphone = Smartphone(
        "Samsung",
        "Смартфон",
        100000.0,
        5,
        "Высокая",
        "S23 Ultra",
        256,
        "Черный",
    )

    assert smartphone.name == "Samsung"
    assert smartphone.efficiency == "Высокая"
    assert smartphone.model == "S23 Ultra"
    assert smartphone.memory == 256
    assert smartphone.color == "Черный"


def test_lawn_grass_initialization():
    grass = LawnGrass(
        "Газон",
        "Трава",
        500.0,
        10,
        "Россия",
        "7 дней",
        "Зеленый",
    )

    assert grass.country == "Россия"
    assert grass.germination_period == "7 дней"
    assert grass.color == "Зеленый"


def test_add_same_products():
    smartphone_1 = Smartphone(
        "Samsung",
        "Смартфон",
        100000.0,
        2,
        "Высокая",
        "S23",
        256,
        "Черный",
    )

    smartphone_2 = Smartphone(
        "Iphone",
        "Смартфон",
        120000.0,
        1,
        "Высокая",
        "15",
        128,
        "Белый",
    )

    assert smartphone_1 + smartphone_2 == 320000.0


def test_add_different_products():
    smartphone = Smartphone(
        "Samsung",
        "Смартфон",
        100000.0,
        2,
        "Высокая",
        "S23",
        256,
        "Черный",
    )

    grass = LawnGrass(
        "Газон",
        "Трава",
        500.0,
        10,
        "Россия",
        "7 дней",
        "Зеленый",
    )

    try:
        smartphone + grass
        assert False
    except TypeError:
        assert True


def test_add_invalid_product():
    category = Category(
        "Категория",
        "Описание",
        [],
    )

    try:
        category.add_product("не продукт")
        assert False
    except TypeError:
        assert True


def test_product_mixin_print(capsys):
    Product(
        "Телефон",
        "Смартфон",
        50000,
        10,
    )

    captured = capsys.readouterr()

    assert "Создан объект Product" in captured.out


def test_product_zero_quantity():
    try:
        Product(
            "Телефон",
            "Смартфон",
            50000.0,
            0,
        )
        assert False
    except ValueError as error:
        assert str(error) == (
            "Товар с нулевым количеством не может быть добавлен"
        )


def test_average_price():
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

    assert category.average_price() == 75000.0


def test_average_price_empty_category():
    category = Category(
        "Пустая категория",
        "Без товаров",
        [],
    )

    assert category.average_price() == 0
