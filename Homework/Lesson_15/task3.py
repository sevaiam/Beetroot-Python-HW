# Task 3
# Product Store
# Write a class Product that has three attributes:
# type
# name
# price
# Then create a class ProductStore, which will have some Products and will operate with all products in the store.
# All methods, in case they can’t perform its action, should raise ValueError with appropriate error information.
# Tips: Use aggregation/composition concepts while implementing the ProductStore class. You can also implement
# additional classes to operate on a certain type of product, etc.
# Also, the ProductStore class must have the following methods:
# add(product, amount) - adds a specified quantity of a single product with a predefined price premium
# for your store(30 percent)
# set_discount(identifier, percent, identifier_type=’name’) - adds a discount for all products specified
# by input identifiers (type or name). The discount must be specified in percentage
# sell_product(product_name, amount) - removes a particular amount of products from the store if available,
# in other case raises an error. It also increments income if the sell_product method succeeds.
# get_income() - returns amount of many earned by ProductStore instance.
# get_all_products() - returns information about all available products in the store.
# get_product_info(product_name) - returns a tuple with product name and amount of items in the store.


class Product:

    def __init__(self, types, name, price):
        self.types = types
        self.name = name
        self.price = price
        self.amount = 0

    def __repr__(self):
        return f'<Name: {self.name}, Type: {self.types}, Price: {self.price}, Amount: {self.amount}>'


class ProductStore:

    def __init__(self):
        self.list_of_products = []
        self.price_for_store = 30
        self.income = 0

    def add(self, product, amount):
        if amount % 1 != 0:
            raise ValueError('Can\'t add non-integer amount.')
        elif amount <= 0:
            raise ValueError('Can\'t add non-positive amount.')
        else:
            product.price *= 1 + (self.price_for_store / 100)
            product.amount = amount
            self.list_of_products.append(product)

    def set_discount(self, identifier, percent, identifier_type='name'):
        if identifier_type == 'name':
            for product in self.list_of_products:
                if product.name == identifier:
                    product.price -= product.price * (percent/100)
        elif identifier_type == 'type':
            for product in self.list_of_products:
                if product.types == identifier:
                    product.price *= product.price * (percent/100)
        else:
            raise ValueError('No identifier found.')

    def sell_product(self, product_name, amount):
        for product in self.list_of_products:
            if product.name == product_name:
                if product.amount >= amount:
                    product.amount -= amount
                    self.income += amount * product.price
                else:
                    raise ValueError('Not enough products.')
        result_list_of_products = [product for product in self.list_of_products if product.amount != 0]
        self.list_of_products = result_list_of_products

    def get_income(self):
        return self.income

    def get_all_products(self):
        return self.list_of_products

    def get_product_info(self, product_name):
        for product in self.list_of_products:
            if product.name == product_name:
                return product.name, product.amount


s = ProductStore()
p = Product

p1 = Product('Sport', 'Football T-Shirt', 100)
p2 = Product('Food', 'Ramen', 1.5)
s.add(p1, 10)
s.add(p2, 300)
s.sell_product('Ramen', 10)
assert s.get_product_info('Ramen') == ('Ramen', 290)
print(s.get_income())
print(s.get_product_info('Ramen'))
print(s.get_product_info('Football T-Shirt'))
print(s.get_all_products())
