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
        print(f"Produktat '{name}' beshe dobaven/obnoven uspeshno.")

    def remove_product(self, name):
        if name in self.products:
            del self.products[name]
            print(f"Produktat '{name}' beshe premahнат.")
        else:
            print("Takav produkt ne sushtestvuva.")

    def search_product(self, name):
        if name in self.products:
            product = self.products[name]
            print(f"Produkt: {name}")
            print(f"Kolichestvo: {product['quantity']}")
            print(f"Cena: {product['price']:.2f} lv.")
        else:
            print("Produktat ne e nameren.")

    def show_all_products(self):
        if not self.products:
            print("Skladat e prazen.")
        else:
            print("\n--- Vsichki produkti v sklada ---")
            for name, info in self.products.items():
                print(f"{name} | Kolichestvo: {info['quantity']} | Cena: {info['price']:.2f} lv.")

    def total_value(self):
        total = 0
        for product in self.products.values():
            total += product["quantity"] * product["price"]
        print(f"Obshta stoynost na sklada: {total:.2f} lv.")
