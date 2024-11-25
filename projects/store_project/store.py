import random
from prettytable import PrettyTable


class store:
    products = [
        {"Name": "water", "price": 80.0, "quantity": 1200},
        {"Name": "soda", "price": 130.0, "quantity": 1200},
        {"Name": "chips", "price": 75.0, "quantity": 1200},
        {"Name": "bread", "price": 45.0, "quantity": 1200},
        {"Name": "eggs", "price": 65.0, "quantity": 1200},
    ]

    def show_products(cls, fields, contents):
        table = PrettyTable()
        table.field_names = fields
        for product in contents:
            table.add_row(product)
        return table

    def show_all_products(cls):
        return cls.show_products(
            ["Name", "price", "quantity"],
            [
                [product["Name"], product["price"], product["quantity"]]
                for product in cls.products
            ],
        )

    def search_products(cls, product_name):
        prd = product_name.lower()
        for i in range(len(cls.products)):
            if prd in cls.products[i]["Name"].lower():
                return cls.show_products(
                    ["Name", "price", "quantity"],
                    [
                        [
                            cls.products[i]["Name"],
                            cls.products[i]["price"],
                            cls.products[i]["quantity"],
                        ]
                    ],
                )
        else:
            return f"{product_name} was not found"
