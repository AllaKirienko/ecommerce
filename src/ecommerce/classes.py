from abc import ABC, abstractmethod


class BaseProduct(ABC):

    @abstractmethod
    def __str__(self):
        pass


class PrintMixin:

    def __init__(self, *args, **kwargs):
        print(
            f"Создан объект {self.__class__.__name__}"
            f" с параметрами {args}"
        )


class Product(PrintMixin, BaseProduct):

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
    ):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

        super().__init__()

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price > 0:
            self.__price = new_price
        else:
            print("Цена не должна быть нулевая или отрицательная")

    def __str__(self):
        return (
            f"{self.name}, {self.price} руб. "
            f"Остаток: {self.quantity} шт."
        )

    def __add__(self, other):
        if type(self) is not type(other):
            raise TypeError(
                "Можно складывать только одинаковые типы продуктов"
            )

        return self.price * self.quantity + other.price * other.quantity

    @classmethod
    def new_product(cls, product_dict):
        return cls(
            product_dict["name"],
            product_dict["description"],
            product_dict["price"],
            product_dict["quantity"],
        )


class Category:
    category_count = 0
    product_count = 0

    def __init__(
        self,
        name: str,
        description: str,
        products: list[Product],
    ):
        self.name = name
        self.description = description
        self._products = products

        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только продукты")

        self._products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        return "\n".join(str(product) for product in self._products)

    def __str__(self):
        total_quantity = sum(product.quantity for product in self._products)
        return f"{self.name}, количество продуктов: " f"{total_quantity} шт."


class Smartphone(Product):

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: str,
        model: str,
        memory: int,
        color: str,
    ):
        super().__init__(
            name,
            description,
            price,
            quantity,
        )
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ):
        super().__init__(
            name,
            description,
            price,
            quantity,
        )
        self.country = country
        self.germination_period = germination_period
        self.color = color
<<<<<<< HEAD
=======

>>>>>>> main
