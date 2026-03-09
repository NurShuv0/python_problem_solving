class Menu:
    def __init__(self):
        self.items = {
            "Burger": 150,
            "Pizza": 300,
            "Pasta": 200,
            "Coffee": 80
        }

    def show_menu(self):
        print("------ MENU ------")
        for item, price in self.items.items():
            print(item, ":", price)


class Order:
    def __init__(self):
        self.orders = {}

    def add_item(self, item, price, quantity):
        self.orders[item] = (price, quantity)

    def show_order(self):
        print("\nYour Order:")
        for item, value in self.orders.items():
            price, quantity = value
            print(item, "x", quantity, "=", price * quantity)

    def total_bill(self):
        total = 0
        for price, quantity in self.orders.values():
            total += price * quantity
        return total


class Restaurant:
    def __init__(self):
        self.menu = Menu()
        self.order = Order()

    def start(self):
        self.menu.show_menu()

        while True:
            item = input("Enter item name (or 'done'): ")

            if item.lower() == "done":
                break

            if item in self.menu.items:
                quantity = int(input("Enter quantity: "))
                price = self.menu.items[item]

                self.order.add_item(item, price, quantity)

            else:
                print("Item not available!")

        self.order.show_order()
        print("Total Bill =", self.order.total_bill())


restaurant = Restaurant()
restaurant.start()