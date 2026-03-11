from food_item import FoodItem
from menu import Menu
from users import Customer, admin, employee
from restaurant import Restaurant
from orders import Order

nur_restaurant = Restaurant("Haruner Bhater Hotel")


def customer_menu():
    name = input("Enter your Name : ")
    email = input("Enter your email : ")
    phone = input("Enter your phone : ")
    address = input("Enter your address : ")
    customer = Customer(name = name, email = email, phone = phone, address=address)

    while True:
        print(f"Welcome {customer.name}!!")
        print("1. View Menu")
        print("2. Add item to cart")
        print("3. View Cart")
        print("4. PayBill")
        print("5. Exit")

        choice = int(input("Enter your choice : "))
        if choice == 1:
            customer.view_menu(nur_restaurant)
        elif choice == 2:
            item_name = input("Enter item name : ")
            item_quantity = int(input("Enter item quatity : "))
            customer.add_to_cart(nur_restaurant, item_name, item_quantity)
        elif choice == 3:
            customer.view_cart()
        elif choice == 4:
            customer.pay_bill()
        elif choice == 5: 
            break
        else : 
            print("Invalid input!!!")



def admin_menu():
    name = input("Enter your Name : ")
    email = input("Enter your email : ")
    phone = input("Enter your phone : ")
    address = input("Enter your address : ")
    adm = admin(name = name, email = email, phone = phone, address=address)

    while True:
        print(f"Welcome {adm.name}!!")
        print("1. Add new item")
        print("2. Add new Employee")
        print("3. View Employee")
        print("4. View items")
        print("5. Delete items ")
        print("6. Exit")

        choice = int(input("Enter your choice : "))
        if choice == 1:
            item_name = input("Enter Item Name : ")
            item_price = input("Enter item price : ")
            item_quantity = input("Enter item quantity : ")
            item = FoodItem(item_name, item_price, item_quantity)
            adm.add_new_item(nur_restaurant, item)
        elif choice == 2:
            name = input("Enter employee name : ")
            phone = input("Enter Phone number : ")
            email = input("Enter email : ")
            designation = input("Enter designation : ")
            age = input("Enter employee age : ")
            salary = input("Enter salary : ")
            address = input("Enter address : ")
            employee_obj = employee(name, email, phone, address, age, designation, salary)
            adm.add_employee(nur_restaurant, employee_obj)

        elif choice == 3:
            adm.view_employee(nur_restaurant)
        elif choice == 4:
            adm.view_menu(nur_restaurant)
        elif choice == 5:
            item_name = input("Enter the item name : ")
            adm.remove_item(nur_restaurant,item_name)
        elif choice == 6:
            break
        else : 
            print("Invalid input!!!")

while True:
    print("welcome!!")
    print("1. Customer")
    print("2. Admin")
    print("3. Exit")
    choice = int(input("Enter your choice : "))
    if choice == 1:
        customer_menu()
    elif choice == 2:
        admin_menu()
    elif choice == 3:
        break
    else : 
        print("Invalid input.Enter valid number!!")
    
