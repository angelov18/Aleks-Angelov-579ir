class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, name, quantity, price):
        if name in self.products:
            self.products[name]["quantity"] += quantity
            self.products[name]["price"] = price
        else:
            self.products[name] = {
                "quantity": quantity,
                "price": price
            }

    def remove_product(self, name):
        if name in self.products:
            del self.products[name]
            print("Produktat beshe premahнат.")
        else:
            print("Produktat ne sushtestvuva.")

    def search_product(self, name):
        if name in self.products:
            print(self.products[name])
        else:
            print("Produktat ne e nameren.")

    def show_products(self):
        if not self.products:
            print("Nyama nalichni produkti.")
        else:
            for name, info in self.products.items():
                print(f"{name} -> Kolichestvo: {info['quantity']} | Cena: {info['price']} lv.")
