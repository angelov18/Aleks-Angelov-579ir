from models import Inventory


def main():
    inventory = Inventory()

    while True:
        print("\n===== SKLADOVA NALICHNOST =====")
        print("1. Dobavi produkt")
        print("2. Premahni produkt")
        print("3. Tarsi produkt")
        print("4. Pokazhi vsichki produkti")
        print("5. Obshta stoynost na sklada")
        print("6. Izhod")

        choice = input("Izberi opciya: ")

        if choice == "1":
            name = input("Ime na produkt: ")

            try:
                quantity = int(input("Kolichestvo: "))
                price = float(input("Cena: "))
                inventory.add_product(name, quantity, price)
            except ValueError:
                print("Molya vuvedi pravilni chisla za kolichestvo i cena.")

        elif choice == "2":
            name = input("Ime na produkt za premahvane: ")
            inventory.remove_product(name)

        elif choice == "3":
            name = input("Ime na produkt za tarsene: ")
            inventory.search_product(name)

        elif choice == "4":
            inventory.show_all_products()

        elif choice == "5":
            inventory.total_value()

        elif choice == "6":
            print("Programata prikluchi.")
            break

        else:
            print("Nevalidna opciya. Opitai otnovo.")


if __name__ == "__main__":
    main()
