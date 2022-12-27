class Shop:
    def __init__(self, name, address, area, category='groceries'):
        self.name = name
        self.address = address
        self.items = {}
        self.area = area
        self.category = category
        self.is_open = True

    def open(self):
        self.is_open = True

    def close(self):
        self.is_open = False

    def supply(self, supplies: dict):
        for i, v in supplies.items():
            if i in self.items:
                self.items[i] += v
            else:
                self.items[i] = v
            print(f"Added {v} of {i} to stock.")

    def sell(self, items: dict):
        for i, v in items.items():
            if i in self.items and v <= self.items[i]:
                self.items[i] -= v
                print(f"Sold {v} of {i}.")
            else:
                print(f"Not enough {i} to sell.")

    def serve_customer(self):
        produce = input(f"What do you want to buy in {self.name}? ")
        amt = int(input("How much do you want to buy? "))
        self.sell({produce: amt,})

    def show_stock(self):
        for i, v in self.items.items():
            print(f"{v} of {i} in stock")


def main():
    silpo = Shop('Silpo', 'Franz Boulevard', 500)
    supplies = {'Carrots': 500, 'Apples': 600, 'Beer': 50}
    silpo.supply(supplies)
    silpo.show_stock()
    shopping_list = {"Carrots": 8, "Apples": 5, "Beer": 1, 'Vodka': 10}
    silpo.sell(shopping_list)
    silpo.serve_customer()
    kopeika = Shop("Kopeika", 'Shevchenko', 300)
    kopeika.supply(supplies)
    kopeika.serve_customer()


if __name__ == "__main__":
    main()
