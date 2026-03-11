from abc import ABC
from orders import Order
class user(ABC):
    def __init__(self, name,email,phone, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class Customer(user):
    def __init__(self, name, email, phone, address):
        super().__init__(name,email, phone, address)
        self.cart = Order()

    def view_menu(self, restaurant):
        restaurant.menu.show_menu()

    def add_to_cart(self, restaurant, item_name, quantity):
        item = restaurant.menu.find_item(item_name)
        # print(f"item quantity is {item.quantity}")
        if item:
            if quantity > item.quantity:
                print("item quantity is exceeded!!!")
            else :
                item.quantity = quantity
                self.cart.add_item(item)
                print("Item added successfully!!")
        else:
            print("item not found")

    def view_cart(self):
        print("**view cart**")
        print("Name\tprice\tquantity")
        for item, quantity in self.cart.items.items():
            print(f"{item.name}\t{item.price}\t{quantity}")
            # print("Item added successfully!!")
        print(f"Total price : {self.cart.total_price}")

    def pay_bill(self):
        print(f'Total {self.cart.total_price} paid successfully!!!')
        self.cart.clear()

class employee(user):
    def __init__(self, name, email, phone, address, age, designation, salary):
        super().__init__(name,email, phone, address)
        self.age = age
        self.designation = designation
        self.salary = salary

# emp = employee("nur", "nur@gmal.com", 1837783561, "dhaka", 23, "chef", 20000)
# print(emp.age)
# print(emp.name)

class admin(user):
    def __init__(self, name, email,phone, address):
        super().__init__(name,email,phone, address)
        # self.employees = []  #database static

    # def add_employee(self, name, email, phone, address, age, designation, salary):
    #     employe = employee(name, email, phone, address, age, designation, salary)#object of employee class
    #     self.employees.append(employe)
    #     print(f"{employe.name} is added!!")

    def add_employee(self, restaurant, employee_obj):
        restaurant.add_employee(employee_obj)

    # def view_employee(self):
    #     print("Employee list : ")
    #     for emp in self.employees:
    #         print(emp.name, emp.email, emp.phone, emp.address)

    def view_employee(self, restaurant):
        restaurant.view_employee()

    def add_new_item(self, restaurant, item):
        restaurant.menu.add_menu_item(item)

    def remove_item(self, restaurant, item):
        restaurant.menu.remove_item(item)

    def view_menu(self, restaurant):
        restaurant.menu.show_menu()





        



# adm = admin("nur_admin", "nur@gmail.com", 18923892, "dhaka")
# adm.add_employee("nur_employee", "employee@gmail.com", 287392, "bosti", 30, "waiter", 10000)
# adm.view_employee()

# Nur_res = Restaurant("Harun er vhater hotel")

# mn = Menu()
# item = FoodItem("pizza", 500, 15)
# item2 = FoodItem("burger", 100, 10)
# item3 = FoodItem("biriyani", 300, 5)
# admin1 = admin("nur_admin", "nur@gmail.com", 89789676, "rupnagar")
# admin1.add_new_item(Nur_res, item)
# admin1.add_new_item(Nur_res, item2)

# mn.add_menu_item(item)
# mn.add_menu_item(item2)
# mn.add_menu_item(item3)
# # mn.show_menu()
# customer1 = Customer("nur_customer", "nur@gmail.com", 89789676, "rupnagar")
# customer1.view_menu(Nur_res)

# item_name = input("Enter item Name : ")
# item_quantity = int(input("Enter item quantity : "))

# customer1.add_to_cart(Nur_res, item_name, item_quantity)
# customer1.view_cart()