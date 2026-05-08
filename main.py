from models import Inventory
from colorama import Fore, init

init(autoreset=True)

inventory = Inventory()

while True:
    print(Fore.CYAN + "\n===== SKLADOVA NALICHNOST =====")
    print("1. Dobavi produkt")
    print("2. Premahni produkt")
    print("3. Tarsi produkt")
    print("4. Pokazhi vsichki produkti")
    print("5. Izhod")

    choice = input("Izberi opciya: ")

    if choice == "1":
        name = input("Ime na produkt: ")
        quantity = int(input("Kolichestvo: "))
        price = float(input("Cena: "))
        inventory.add_product(name, quantity, price)
        print(Fore.GREEN + "Produktat beshe dobaven.")

    elif choice == "2":
        name = input("Ime na produkt: ")
        inventory.remove_product(name)

    elif choice == "3":
        name = input("Ime na produkt: ")
        inventory.search_product(name)

    elif choice == "4":
        inventory.show_products()

    elif choice == "5":
        print(Fore.RED + "Programata priklyuchi.")
        break

    else:
        print("Nevalidna opciya.")
