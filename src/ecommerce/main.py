from ecommerce.classes import Category, Product


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

    category = Category(
        "Смартфоны",
        (
            "Смартфоны, как средство не только коммуникации, "
            "но и получения дополнительных функций для удобства жизни"
        ),
        [product1, product2],
    )

    print(category.name)
    print(category.description)
    print(len(category.products))
    print(Category.category_count)
    print(Category.product_count)
    print(product1)
    print(product2)
    print(category)
    print(product1 + product2)


if __name__ == "__main__":
    main()
