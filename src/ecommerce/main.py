from ecommerce.classes import Category, LawnGrass, Product, Smartphone


def main():
    product1 = Product(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
    )

    product2 = Product(
        "Iphone 15",
        "512GB, Gray space",
        210000.0,
        8,
    )

    product3 = Smartphone(
        "Samsung Galaxy S24",
        "512GB, Black",
        190000.0,
        4,
        "Высокая",
        "S24",
        512,
        "Черный",
    )

    product4 = LawnGrass(
        "Газонная трава",
        "Для дачи",
        500.0,
        20,
        "Россия",
        "7 дней",
        "Зеленый",
    )

    category1 = Category(
        "Смартфоны",
        (
            "Смартфоны, как средство не только коммуникации, "
            "но и получения дополнительных функций для удобства жизни"
        ),
        [product1, product2, product3],
    )

    category2 = Category(
        "Газонная трава",
        "Товары для сада",
        [product4],
    )

    print(category1.name)
    print(category1.description)
    print(category1.products)
    print(category1)

    print(category2.name)
    print(category2.description)
    print(category2.products)
    print(category2)

    print(Category.category_count)
    print(Category.product_count)

    print(product1 + product2)


if __name__ == "__main__":
    main()
