from menu import Menu

class Restaurant():
    def __init__(self, name):
        self.name = name 
        self.employees = []  #database static
        self.menu = Menu()

    def add_employee(self, employee_obj):
        self.employees.append(employee_obj)

    def view_employee(self):
        print("Employee list : ")
        for emp in self.employees:
            print(emp.name, emp.email, emp.phone, emp.address)
