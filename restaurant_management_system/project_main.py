from abc import ABC

class user(ABC):
    def __init__(self, name,email,phone, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address


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

class Restaurant():
    def __init__(self, name):
        self.name = name 
        self.employees = []  #database static

    def add_employee(self, employee_obj):
        self.employees.append(employee_obj)

    def view_employee(self):
        print("Employee list : ")
        for emp in self.employees:
            print(emp.name, emp.email, emp.phone, emp.address)

class Menu:
    def __init__(self):
        self.items = []

    def add_menu_item(self, item):
        self.items.append(item)

    def find_item(self, item_name):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                return item
            
        return None
    def remove_item(self, item_name):
        item = self.find_item(item_name)
        if item:
            self.items.remove(item)
            print("item is found and deleted!!")
        else :
            print("item is not found!!")

    def show_menu(self):
        print("***Menu item are***")
        print("Name\tprince\tQuantity")
        for item in self.items:
            print(f'{item.name}\t{item.price}\t{item.quantity}')

class FoodItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        



# adm = admin("nur_admin", "nur@gmail.com", 18923892, "dhaka")
# adm.add_employee("nur_employee", "employee@gmail.com", 287392, "bosti", 30, "waiter", 10000)
# adm.view_employee()

mn = Menu()
item = FoodItem("pizaa", 100, 10)
mn.add_menu_item(item)
mn.show_menu()

